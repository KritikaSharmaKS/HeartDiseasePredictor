var socket = io.connect('http://' + "127.0.0.1" + ':' + "5000");
    socket.on('connect', function() {
		alert("connected");
		
        
    });
	socket.on('disconnect', function() {
		alert("disconnected");
		
        
    });
	function send_message(){
		socket.send("asfd");
		alert("sent");
	}
	
	socket.on('message', function(data) {
        if(data[0] == "processed_data"){
			alert(data[1])
		}
    });