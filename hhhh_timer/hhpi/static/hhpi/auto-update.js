$(function worker() {
    $.ajax({
	url: 'hhpi/results.html',
	success: function(data){
	    $('.result').html(data);
	    console.log("Here we go with another page.");
	},
	complete: function() {
	    setTimeout(worker, 10000);
	}
    }); 
});