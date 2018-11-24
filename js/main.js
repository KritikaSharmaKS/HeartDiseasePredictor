$(document).ready(function(){
	$( "#send_data" ).click(function() {
		collect_data();
	});
});

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

function collect_data(){
	let gender = $('input[name=gender]:checked').val();
	let chest_pain = $('#cp').attr('selected','selected').val();
	let age = $("#age").val();
	let resting_bp = $("#rbp").val();
	let chol = $("#chol").val();
	let fbs = $('input[name=fbs]:checked').val();
	let restecg = $('input[name=restecg]:checked').val();
	let thalach = $("#thalach").val();
	let exang = $('input[name=exang]:checked').val();
	let oldpeak = $("#oldpeak").val();
	let slope = $('input[name=slope]:checked').val();
	let ca = $("#ca").val();
	let thal = $("#thal").val();
	let num = $('input[name=num]:checked').val();
} 

socket.on('message', function(data) {
	if(data[0] == "processed_data"){
		alert(data[1])
	}
});


