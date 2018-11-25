$(document).ready(function(){
	$( "#send_data" ).click(function() {
		collect_data();
	});
});
$(document).ready(function(){
	$( "#send_less_data" ).click(function() {
		collect_less_data();
	});
});

$("#formfordoc").click(function(){
	$('#exampleModalLong').modal('show');
});

$("#formforelse").click(function(){
	$('#exampleModalLong2').modal('show');
});


var socket = io.connect('http://' + "127.0.0.1" + ':' + "5000");
socket.on('connect', function() {
	alert("connected");
	
	
});
socket.on('disconnect', function() {
	alert("disconnected");
	
});
function send_message(dataToBeSent){
	alert("in send_message");
	socket.emit("form data", dataToBeSent);
	alert("sent");
}

function collect_data(){
	alert("inside collect_data");
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
	let myObject = {
		genderKey: gender,
		cp: chest_pain,
		ageKey: age,
		rbp: resting_bp,
		cholKey: chol,
		fbsKey: fbs,
		restecgKey: restecg,
		thalachKey: thalach,
		exangKey: exang,
		oldpeakKey: oldpeak,
		slopeKey: slope,
		caKey: ca,
		thalKey: thal,
		numKey: num
	};
	alert("inside collect_data 2");
	send_message(myObject);
} 


function collect_less_data(){
	alert("inside collect_data");
	let gender = $('input[name=gender]:checked').val();
	let chest_pain = $('#cp').attr('selected','selected').val();
	let age = $("#age").val();
	let resting_bp = $("#rbp").val();
	let chol = $("#chol").val();
	let fbs = $('input[name=fbs]:checked').val();
	/*let restecg = $('input[name=restecg]:checked').val();*/
	let thalach = $("#thalach").val();
	/*let exang = $('input[name=exang]:checked').val();
	let oldpeak = $("#oldpeak").val();*/
	/*let slope = $('input[name=slope]:checked').val();*/
	/*let ca = $("#ca").val();
	let thal = $("#thal").val();*/
	let num = $('input[name=num]:checked').val();
	let myObject = {
		genderKey: gender,
		cp: chest_pain,
		ageKey: age,
		rbp: resting_bp,
		cholKey: chol,
		fbsKey: fbs,
		/*restecgKey: restecg,*/
		thalachKey: thalach,
		/*exangKey: exang,
		oldpeakKey: oldpeak,
		slopeKey: slope,
		caKey: ca,
		thalKey: thal,*/
		numKey: num
	};
	alert("inside collect_data 2");
	send_message(myObject);
} 




socket.on('message', function(data) {
	alert("hello test");
	if(data[0] == "Result"){
		alert(data[1])
	}
});


