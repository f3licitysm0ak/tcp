import json

#in-memory database
notes = {}
next_id = 1

def handle_request(connection):
    #1. read http headers until \r\n\r\n
    raw_headers = ""
    while not raw_headers.endswith("\r\n\r\n"):
        chunk = connection.recv(1).decode("utf-8", errors="ignore")
        if not chunk:
            return
        raw_headers += chunk

    #separate request line + headers from header-terminator
    headers_part = raw_headers[:-4]
    lines = headers_part.split("\r\n")
    
    #parse request line
    request_line = lines[0].split(" ")
    if len(request_line) < 3:
        return
    method = request_line[0]
    path = request_line[1]
    version = request_line[2]

    #parse headers into a dictionary
    headers = {}
    for line in lines[1:]:
        if ": " in line:
            key, val = line.split(": ", 1)
            headers[key.lower()] = val

    #2. read request body if content-length exists
    body_str = ""
    if "content-length" in headers:
        content_length = int(headers["content-length"])
        for _ in range(content_length):
            body_str += connection.recv(1).decode("utf-8", errors="ignore")

    #3. rest routing logic
    global next_id
    status_code = "200 OK"
    response_body = ""

    #route: /notes
    if path == "/notes":
        if method == "GET":
            #return list of all notes
            status_code = "200 OK"
            response_body = json.dumps(list(notes.values()))
            
        elif method == "POST":
            #create a new note
            try:
                data = json.loads(body_str) if body_str else {}
                note = {
                    "id": next_id,
                    "title": data.get("title", ""),
                    "body": data.get("body", "")
                }
                notes[next_id] = note
                next_id += 1
                
                status_code = "201 Created"
                response_body = json.dumps(note)
            except json.JSONDecodeError:
                status_code = "400 Bad Request"
                response_body = json.dumps({"error": "Invalid JSON"})
        else:
            status_code = "405 Method Not Allowed"
            response_body = json.dumps({"error": "Method not allowed"})

    #route: /notes/{id}
    elif path.startswith("/notes/"):
        parts = path.split("/")
        note_id_str = parts[2] if len(parts) > 2 else ""

        if not note_id_str.isdigit():
            status_code = "400 Bad Request"
            response_body = json.dumps({"error": "Invalid note ID"})
        else:
            note_id = int(note_id_str)

            if note_id not in notes:
                status_code = "404 Not Found"
                response_body = json.dumps({"error": "Note not found"})
            elif method == "GET":
                status_code = "200 OK"
                response_body = json.dumps(notes[note_id])
            elif method == "PUT":
                try:
                    data = json.loads(body_str) if body_str else {}
                    notes[note_id]["title"] = data.get("title", notes[note_id]["title"])
                    notes[note_id]["body"] = data.get("body", notes[note_id]["body"])
                    
                    status_code = "200 OK"
                    response_body = json.dumps(notes[note_id])
                except json.JSONDecodeError:
                    status_code = "400 Bad Request"
                    response_body = json.dumps({"error": "Invalid JSON"})
            elif method == "DELETE":
                del notes[note_id]
                status_code = "200 OK"
                response_body = json.dumps({"message": f"Note {note_id} deleted"})
            else:
                status_code = "405 Method Not Allowed"
                response_body = json.dumps({"error": "Method not allowed"})
    else:
        status_code = "404 Not Found"
        response_body = json.dumps({"error": "Endpoint not found"})

    #4. construct & send http response
    response = (
        f"HTTP/1.1 {status_code}\r\n"
        f"Content-Type: application/json\r\n"
        f"Content-Length: {len(response_body.encode('utf-8'))}\r\n"
        f"Connection: close\r\n\r\n"
        f"{response_body}"
    )
    
    connection.sendall(response.encode("utf-8"))