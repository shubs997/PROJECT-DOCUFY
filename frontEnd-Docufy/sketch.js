let dropzone;
let data;
let dataURL;
let hashValue;


console.log("sketchdfs");
function setup() {
  // createCanvas(200, 200);
  // background(0);
  
  dropzone = select('#dropzone');
  dropzone.dragOver(highlight);
  dropzone.dragLeave(unhighlight);
  dropzone.drop(gotFile, unhighlight);
    
}

function gotFile(file) {
  // createP(file.name + " " + file.size);
  // var img = createImg(file.data);
  // img.size(100, 100);
  
  // If it's an image file
  if (file.type === 'image') {
    // Create an image DOM element but don't show it
    // const img = createImg(file.data);
    dataURL = file.data;
    console.log(dataURL)
    base64Image = dataURL.replace(/^data:image.+;base64,/, '');
    console.log("testing func");
    //console.log(base64Image);

    console.log("storing base64Image in request message..");

    let message = {
      image: base64Image
    }
    message = JSON.stringify(message);
    console.log("...SENDING FINAL REQUEST MESSAGE...")
    //console.log(message);
    console.log(typeof message)

    $.ajax({
      url:"http://3.23.44.163/predict",
      method:"POST",
      data: message,
      contentType: false,
      crossDomain: true,
      cache: false,
      processData: false,  
      success:function(data)
      {
        console.log(data);
        $("#verify").click(function(data){
          verifyPopulate(data);
        })
        setTimeout(function() {
          changeToResult(data);
          displayoriginal(dataURL);
          plot(data);
      }, 6000)
      //  alert(data);
      }
     });
    typeof(img);
    document.getElementById("changeText").innerHTML = "Uploading...";
    //start progress bar
    progress();
    //call change function 
    setTimeout(change, 5000);
    // setTimeout(changeToResult(data), 10000);
    // Draw the image onto the canvas
    // image(img, 0, 0, width, height);
  } else {
    document.getElementById("changeText").innerHTML = "Not an image file! upload png and jpg files only.";
    console.log('Not an image file!');
  }
}












function highlight() {
  dropzone.style('background-color', '#ccc');
  
}

function unhighlight() {
  dropzone.style('background-color', 'transparent');
  
}

function change() {
  var changeText = document.getElementById("changeText");
  var icon = document.getElementById("icon");

  document.getElementById("load").style.display = 'none';
  document.getElementById("changeText").style.display = 'block';
  document.getElementById("icon").style.display = 'block';

  changeText.innerHTML = "Analyzing with neural network";

  icon.src = "assets/refresh.svg";
  icon.classList.add('spin');
}


function changeToResult(data) {  
  var changeText = document.getElementById("changeText"); //main drag n drop text
  var tickCross = document.getElementById("tickCross"); //tick svg
  var displaySpan = document.getElementById("displaySpan"); //prediction display span
  var uploadedImage = document.getElementById("uploadedImage"); //uploaded base64 image
  var elaImage = document.getElementById("elaImage"); //recieved ELA image
  var verify = document.getElementById("verify"); //the verify blockchain button
  var dropzone = document.getElementById("dropzone"); //for result display page
  var colLeft = document.getElementById("colLeft"); //for result display page
  var colLeftText = document.getElementById("colLeftText"); //for result display page
  var textDisplay = document.getElementById("textDisplay");
  //adding css for result display page
  dropzone.style.flexDirection = 'row';
  colLeft.style.backgroundColor = '#ddd';
  colLeft.style.borderRadius = '8px';
  colLeftText.style.display = 'flex';
  textDisplay.style.marginLeft = '10%';
  verify.style.display = 'block';
  
  document.getElementById("displayResult").style.display = 'flex';
  
  document.getElementById("icon").style.display = 'none';
  document.getElementById("load").style.display = 'none';
  document.getElementById("changeText").style.display = 'block';
  document.getElementById("chart-container").style.display = 'block';
  
  Au = data.output.Au;
  Tp = 100 - data.output.Tp;

  var score = "score : "+data.score+ "%";
  hashValue = "Hash: "+data.shahash;
  changeText.innerHTML = score;
  //display cross if manipulated
  if(data.prediction == 'Image Is Manipulated'){
    tickCross.src = "assets/cross.svg";
  }
  uploadedImage.style.display = 'block';
  elaImage.style.display = 'block';
  $(".img_caption").show();
  displaySpan.innerHTML = data.prediction;
  elaImage.src = "data:image/png;base64," + data.ImageBytes;
  
}

function changeToAnalysis(data) {  
  var changeText = document.getElementById("changeText"); //main drag n drop text
  var tickCross = document.getElementById("tickCross"); //tick svg
  var displaySpan = document.getElementById("displaySpan"); //prediction display span
  var uploadedImage = document.getElementById("uploadedImage"); //uploaded base64 image
  var elaImage = document.getElementById("elaImage"); //recieved ELA image
  var verify = document.getElementById("verify"); //the verify blockchain button
  var dropzone = document.getElementById("dropzone"); //for result display page
  var colLeft = document.getElementById("colLeft"); //for result display page
  var colLeftText = document.getElementById("colLeftText"); //for result display page
  var textDisplay = document.getElementById("textDisplay");
  //adding css for result display page
  dropzone.style.flexDirection = 'row';
  colLeft.style.backgroundColor = '#ddd';
  colLeft.style.borderRadius = '8px';
  colLeftText.style.display = 'none';
  textDisplay.style.marginLeft = '10%';
  verify.style.display = 'none';
  $(".resultImages").css("margin-top", "4vh");

  
  document.getElementById("displayResult").style.display = 'flex';
  
  document.getElementById("icon").style.display = 'none';
  document.getElementById("load").style.display = 'none';
  document.getElementById("changeText").style.display = 'block';
  document.getElementById("chart-container").style.display = 'block';
  
  Au = data.output.Au;
  Tp = 100 - data.output.Tp;

  var score = "score : "+data.score+ "%";
  hashValue = "Hash: "+data.shahash;
  changeText.innerHTML = score;
  //display cross if manipulated
  if(data.prediction == 'Image Is Manipulated'){
    tickCross.src = "assets/cross.svg";
  }
  uploadedImage.style.display = 'block';
  elaImage.style.display = 'block';
  $(".img_caption").show();
  displaySpan.innerHTML = data.prediction;
  elaImage.src = "data:image/png;base64," + data.ImageBytes;
  
}

function displayoriginal(dataURL) {
  console.log("DISPLAY ORIGINAL CALLED...");
  var uploadedImage = document.getElementById("uploadedImage"); //uploaded base64 image
  uploadedImage.src = dataURL;
}

function progress(){
  const progressBar = document.getElementsByClassName('progress-bar')[0]
  document.getElementById("load").style.display = 'block';
  document.getElementById("or").style.display = 'none';
  document.getElementById("chooseFile").style.display = 'none';
  setInterval(() => {
    const computedStyle = getComputedStyle(progressBar)
    const width = parseFloat(computedStyle.getPropertyValue('--width')) || 0
    if(width != 100){
      progressBar.style.setProperty('--width', width + .1)
    }
  }, 5)
}

function prepareIssue(data){
  
  document.getElementById("chooseFile").style.display = 'block';
  document.getElementById("or").style.display = 'block';
  document.getElementById("or").style.marginBottom = '0';
  document.getElementById("or").style.fontWeight = 'bold';
  document.getElementById("or").innerHTML = "Drag and drop to upload another file<br> OR";
  
  document.getElementById("load").style.display = 'none';
  var icon = document.getElementById("icon");
  var textbox = document.getElementById("changeText");
  textbox.style.display = 'block';
  textbox.style.fontSize = '1rem';
  
  icon.style.display = 'none';
  
  changeText.innerHTML = data.message+"<br>index: "+data.index+"<br>proof: "+data.proof+"<br>previous_hash: "+data.previous_hash+"<br>img_hash: "+data.img_hash;
}


function prepareCheckResults(data){
  document.getElementById("chooseFile").style.display = 'block';
  document.getElementById("or").style.display = 'block';
  document.getElementById("or").style.marginBottom = '0';
  document.getElementById("or").style.fontWeight = 'bold';
  document.getElementById("or").innerHTML = "Drag and drop to upload another file<br> OR";
  
  document.getElementById("load").style.display = 'none';
  var icon = document.getElementById("icon");
  var textbox = document.getElementById("changeText");
  textbox.style.display = 'block';
  textbox.style.fontSize = '1rem';
  
  icon.style.display = 'none';
  console.log(data);
  changeText.innerHTML = data.message;

}

function verifyPopulate(data) {
  document.getElementById("myHash").innerHTML = hashValue;
  console.log("here comes the hash.."+hashValue)
  if(hashValue != "Hash: "){
    $("#verify").html('Blockchain Verified <i style="color:#1AC05E; font-size: 1rem;" class="fas fa-check-circle"></i>');
    $("#myHash").show();
  } else {
    $("#verify").html('Rejected<i style="color:red; font-size: 1rem;" class="fas fa-times-circle"></i>');
    // $("#myHash").show();
  }

  // $("#myHash")..css({ 'font-size': '1rem' });
}




function plot(data){
  Au = data.output.Au * 100;
  Tp = data.output.Tp * 100;
  console.log("au and tp are:"+data.output)
  let myChart = document.getElementById('myChart').getContext('2d');
  let massPopChart = new Chart(myChart, {
    type:'pie', // bar, horizontalBar, pie, line, doughnut, radar, polarArea
    data:{
      labels:['Authentic', 'Manipulated'],
      datasets:[{
        label:'Population',
        data:[
          Au.toFixed(2),
          Tp.toFixed(2)
        ],
        //backgroundColor:'green',
        backgroundColor:[
          '#007E97',
          '#00d0ff',
        ],
        borderWidth:0,
        borderColor:'#777',
        hoverBorderWidth:1,
        hoverBorderColor:'#000'
      }]
    },
    options:{
      legend:{
        display:false,
        position:'right',
      },
      layout: {
        padding: {
            left: 10,
            right: 10
        }
    },
      tooltips:{
        yAlign: 'bottom',
      }
    }
  });
}


