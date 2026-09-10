def receive_message(connection):

    content_length = False
    content_idx = -1
    line = 0
    curr_string = ""
    while True:
        curr_string += connection.recv(1).decode()
        if (curr_string[0:14].lower() == "content_length"):
            content_length = True;
        if (curr_string[curr_string.length-4:] == "\r\n\r\n"):
            break;

    curr_string = curr_string[:curr_string.length-4]
    lines = curr_string.split("\r\n")
    #atp we should have an array of most of the lines including content-length, if it exists

    
    #if we have content length, read that many more bytes , otherwise, do nothing
    if (content_length):
        start = curr_string.find("Content-Length: ")
        end = curr_string.find("\r\n", start)
        len_string = curr_string[start+1:end]
        len_num=int(len_string)
        body=""
        for i in range (len_num):
            body += connection.recv(1).decode()


    #now process stuff 
    #get version, reason phrase aka the thing w HTTP, headers n values, optionally the body


    line1 = lines[0]

    line1_arr = line1.split(" ")
    method = line1[0]
    path = line1[1]
    version = line1[2]

    status_code = ""
    body_ = ""

    if (method == "GET"):
        status_code = "200 OK"
        if (path == "/hello"):
            body_= body
        else:
            status_code = "404 Not Found"
            body_ = "Not Found"
    else:
        status_code = "405 Method Not Allowed"

    response = f"HTTP/1.1 {status_code}\r\nContent-Type: text/plain\r\nContent-Length: {len(body_)}\r\n\r\n{body_}"

def send_response(connection, response):
    res = response.encode()
    connection.send(res) 
    