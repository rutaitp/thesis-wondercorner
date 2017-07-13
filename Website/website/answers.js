console.log("hello");

var par;
var container;
var socket;
var headline;
var button;

function setup(){
	noCanvas();

	socket = io.connect();

	socket.on("sending_answers", function(data) {
		console.log(data);

		container = select(".grid");

		var answerLines = data.split();
		console.log(answerLines);

		answerLines = answerLines[0].replace(/(.*\?)(.*)/,'<b>$1</b><br>$2');

		par = createElement("div", answerLines);
			par.class("grid-item");
			par.parent(container);

			var r = floor(random(100, 255));
  			var g = floor(random(150, 255));
  			var b = floor(random(200, 255));
  			par.style('background-color', 'rgb(' + r + ',' + g + ',' + b + ')');

			msnry = new Masonry( ".grid", {
				// options
  	 			itemSelector: '.grid-item', //shows which child in the grid
  	 			percentPosition: true,
  	 			gutter: 10,
  	 			horizontalOrder: true
			});
	});
}

//TO TOP BUTTON
// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("myBtn").style.display = "block";
    } else {
        document.getElementById("myBtn").style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0; // For Chrome, Safari and Opera 
    document.documentElement.scrollTop = 0; // For IE and Firefox
}