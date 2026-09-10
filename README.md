Progression from TCP socket client-server programming to HTTP/RESTful mini-service. <br>

Folders:  <br>
milestone-1: simplest socket program between client and server with echo protocol <br>
milestone-2: length-prefixed framing - sending length, then message so the receiver knows exactly how many bytes to read. <br>
milestone-3: receiving message, parsing line with a specific command (ECHO, TIME, etc.), and sending result of executing that command. <br>
milestone-4: slightly more structured parsing with header, content, etc. that is closer to the real protocol. <br>
milestone-5: RESTful service with http/rest-like formatting and json response.
