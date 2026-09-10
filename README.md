Progression from TCP socket client-server programming to HTTP/RESTful mini-service. 
Folders: 
milestone-1: simplest socket program between client and server with echo protocol
milestone-2: length-prefixed framing - sending length, then message so the receiver knows exactly how many bytes to read.
milestone-3: receiving message, parsing line with a specific command (ECHO, TIME, etc.), and sending result of executing that command.
milestone-4: slightly more structured parsing with header, content, etc. that is closer to the real protocol.
milestone-5: RESTful service with http/rest-like formatting and json response.
