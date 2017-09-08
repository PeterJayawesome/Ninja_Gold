$(document).ready(function(){
	// $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
	$('form').submit(function(){
		$.getJSON('/response',{
			"building":$(this).children("input[name='building']").val()
		},function(res){
			console.log(res)
			$('#gold').html(res.gold)
			if(res.earned >= 0){
				$('#activity').append("<p class = 'blue'>"+res.activity[res.activity.length-1]+"<\p>")
			}
			else{
				$('#activity').append("<p class = 'red'>"+res.activity[res.activity.length-1]+"<\p>")
			}
			// var gold = res.gold
			// if (res.activity.length>0){
			// 	var active = res.activity[res.activity.length-1]
			// 	console.log(active)
			// }
			
			// var earned = res.earned
			// console.log(gold)
			
			// console.log(earned)

		})
		return false
	})
})