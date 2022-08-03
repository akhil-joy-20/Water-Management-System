
//reading percentage data
fetch('percent.txt')
  .then(response => response.text())
  .then(data => {
  	console.log(data);
    document.getElementById("perce").innerText = data+"%";
    document.getElementById("percen").innerText = data+"%";
    document.getElementById("percen").style.width = data + "%";
  });

//reading ph data
fetch('ph.txt')
  .then(response => response.text())
  .then(data => {
  	console.log(data);
    document.getElementById("ph_val").innerText =data;
    data=data*10-20;
    document.getElementById("ph_val").style.width = data + "%";
    // if(data<7)
    //   document.getElementById("ph_val").classList.add("red");
    // else if(data>=7 && data<=8.5)
    //   document.getElementById("ph_val").classList.add("green");
    // document.getElementsByClassName("ph_bar").style.backgroundColor = "red";
  });

//reading ph description
fetch('data.txt')
  .then(response => response.text())
  .then(data => {
  	console.log(data);
    document.getElementById("ph_desc").innerText = data;
  });




