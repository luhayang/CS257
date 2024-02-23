the_heading = document.getElementById("hello");

the_heading.onclick = function(){ the_heading.innerText="Goodbye World!"};

the_paragraph = document.getElementById("paragraph1");

the_paragraph.onmouseenter = function() { 
	the_paragraph.style.color = "blue";
  the_paragraph.style.backgroundColor = "white";
};

function changeColor() {
  text_input_element = document.getElementById("user-color");
  new_color = text_input_element.value;
	the_heading.style.color = new_color;
}

function randNum() {
	num = Math.floor(Math.random() * 100);
  document.getElementById('demo').innerHTML = num
}

function switchColor() {
	document.getElementById("demobox").classList.toggle("switch-mode");  
}

function sentence() {
	text_input = document.getElementById("user-name").value;
  if (text_input == ""){
  	the_sentence = "Type the Name!"
  } else {
  	the_sentence = text_input + " the Brave was born in " + (Math.floor(Math.random() * 101) + 1900) + ".";
  }
  document.getElementById('demo2').innerHTML = the_sentence;
}