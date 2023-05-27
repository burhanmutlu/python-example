
let width = 320;
let height = 0;

// whether streaming video from the camera.
let streaming = false;

let video = document.getElementById("video");
let stream = null;
let vc = null;

function startCamera() {
  if (streaming) return;
  navigator.mediaDevices.getUserMedia({video: true, audio: false})
    .then(function(s) {
    stream = s;
    video.srcObject = s;
    video.play();
  })
    .catch(function(err) {
    console.log("An error occured! " + err);
  });

  video.addEventListener("canplay", function(ev){
    if (!streaming) {
      height = video.videoHeight / (video.videoWidth/width);
      video.setAttribute("width", width);
      video.setAttribute("height", height);
      streaming = true;
      vc = new cv.VideoCapture(video);
    }
    startVideoProcessing();
  }, false);
}

let lastFilter = '';
let src = null;
let dstC1 = null;
let dstC3 = null;
let dstC4 = null;

function startVideoProcessing() {
  if (!streaming) { console.warn("Please startup your webcam"); return; }
  stopVideoProcessing();
  src = new cv.Mat(height, width, cv.CV_8UC4);
  dstC1 = new cv.Mat(height, width, cv.CV_8UC1);
  dstC3 = new cv.Mat(height, width, cv.CV_8UC3);
  dstC4 = new cv.Mat(height, width, cv.CV_8UC4);
  requestAnimationFrame(processVideo);
}

function passThrough(src) {
  return src;
}



function sobel(src) {
  var mat = new cv.Mat(height, width, cv.CV_8UC1);
  cv.cvtColor(src, mat, cv.COLOR_RGB2GRAY, 0);
  cv.Sobel(mat, dstC1, cv.CV_8U, 1, 0, controls.sobelSize, 1, 0, cv.BORDER_DEFAULT);
  mat.delete();
  return dstC1;
}

function scharr(src) {
  var mat = new cv.Mat(height, width, cv.CV_8UC1);
  cv.cvtColor(src, mat, cv.COLOR_RGB2GRAY, 0);
  cv.Scharr(mat, dstC1, cv.CV_8U, 1, 0, 1, 0, cv.BORDER_DEFAULT);
  mat.delete();
  return dstC1;
}

function laplacian(src) {
  var mat = new cv.Mat(height, width, cv.CV_8UC1);
  cv.cvtColor(src, mat, cv.COLOR_RGB2GRAY);
  cv.Laplacian(mat, dstC1, cv.CV_8U, controls.laplacianSize, 1, 0, cv.BORDER_DEFAULT);
  mat.delete();
  return dstC1;
}

function processVideo() {
  stats.begin();
  vc.read(src);
  let result;
  switch (controls.filter) {
    case 'passThrough': result = passThrough(src); break;
    case 'sobel': result = sobel(src); break;
    case 'scharr': result = scharr(src); break;
    case 'laplacian': result = laplacian(src); break;
    case 'backprojection': result = backprojection(src); break;
    case 'erosion': result = erosion(src); break;
    case 'dilation': result = dilation(src); break;
    default: result = passThrough(src);
  }
  cv.imshow("canvasOutput", result);
  stats.end();
  lastFilter = controls.filter;
  requestAnimationFrame(processVideo);
}

function stopVideoProcessing() {
  if (src != null && !src.isDeleted()) src.delete();
  if (dstC1 != null && !dstC1.isDeleted()) dstC1.delete();
  if (dstC3 != null && !dstC3.isDeleted()) dstC3.delete();
  if (dstC4 != null && !dstC4.isDeleted()) dstC4.delete();
}

function stopCamera() {
  if (!streaming) return;
  stopVideoProcessing();
  document.getElementById("canvasOutput").getContext("2d").clearRect(0, 0, width, height);
  video.pause();
  video.srcObject=null;
  stream.getVideoTracks()[0].stop();
  streaming = false;
}

var stats = null;

var filters = {
  'sobel': 'Sobel Derivatives',
  'scharr': 'Scharr Derivatives',
  'laplacian': 'Laplacian Derivatives',
  'backprojection': 'Backprojection'
};

var filterName = document.getElementById('filterName');

var controls;

function initUI() {
  stats = new Stats();
  stats.showPanel(0);
  document.getElementById('container').appendChild(stats.domElement);

  controls = {
    filter: 'passThrough',
    setFilter: function(filter) {
      this.filter = filter;
      filterName.innerHTML = filters[filter];
    },
    passThrough: function() { this.setFilter('passThrough'); },
    gray: function() { this.setFilter('gray'); },
    hsv: function() { this.setFilter('hsv'); },
    inRange: function() { this.setFilter('inRange'); },
    inRangeLow: 75,
    inRangeHigh: 150,
    threshold: function() { this.setFilter('threshold'); },
    thresholdValue: 100,
    adaptiveThreshold: function() { this.setFilter('adaptiveThreshold'); },
    adaptiveBlockSize: 3,
    gaussianBlur: function() { this.setFilter('gaussianBlur'); },
    gaussianBlurSize: 7,
    medianBlur: function() { this.setFilter('medianBlur'); },
    medianBlurSize: 5,
    bilateralFilter: function() { this.setFilter('bilateralFilter'); },
    bilateralFilterDiameter: 5,
    bilateralFilterSigma: 75,
    sobel: function() { this.setFilter('sobel'); },
    sobelSize: 3,
    scharr: function() { this.setFilter('scharr'); },
    laplacian: function() { this.setFilter('laplacian'); },
    laplacianSize: 3,
    canny: function() { this.setFilter('canny'); },
    cannyThreshold1: 150,
    cannyThreshold2: 300,
    cannyApertureSize: 3,
    cannyL2Gradient: false,
    contours: function() { this.setFilter('contours'); },
    contoursMode: cv.RETR_CCOMP,
    contoursMethod: cv.CHAIN_APPROX_SIMPLE,
    calcHist: function() { this.setFilter('calcHist'); },
    equalizeHist: function() { this.setFilter('equalizeHist'); },
    backprojection: function() { this.setFilter('backprojection'); },
    backprojectionRangeLow: 0,
    backprojectionRangeHigh: 150,
    morphology: function () { this.setFilter('morphology'); },
    morphologyShape: cv.MORPH_RECT,
    morphologyOp: cv.MORPH_ERODE,
    morphologySize: 5,
    morphologyBorderType: cv.BORDER_CONSTANT,
  };
  
  let gui = new dat.GUI({ autoPlace: false });
  let guiContainer = document.getElementById('guiContainer');
  guiContainer.appendChild(gui.domElement);
  
  let lastFolder = null;
  function closeLastFolder(folder) {
    if (lastFolder != null && lastFolder != folder) {
      lastFolder.close();
    }
    lastFolder = folder;
  }

  let passThrough = gui.add(controls, 'passThrough').name(filters['passThrough']).onChange(function() {
    closeLastFolder(null);
  });
  
  let colorConversion = gui.addFolder('Color Conversion');
  colorConversion.add(controls, 'gray').name(filters['gray']).onChange(function() {
    closeLastFolder(null);
  });
  
  colorConversion.add(controls, 'hsv').name(filters['hsv']).onChange(function() {
    closeLastFolder(null);
  });
  
  
  let gradients = gui.addFolder('Gradients')
  let sobel = gradients.addFolder(filters['sobel']);
  sobel.domElement.onclick = function() {
    closeLastFolder(sobel);
    controls.sobel();
  };
  sobel.add(controls, 'sobelSize', 3, 19, 1).name('kernel size').onChange(function(value) { if (value % 2 === 0) controls.sobelSize = value + 1;});
  
  gradients.add(controls, 'scharr').name(filters['scharr']).onChange(function() {
    closeLastFolder(null);
  });

  let laplacian = gradients.addFolder(filters['laplacian']);
  laplacian.domElement.onclick = function() {
    closeLastFolder(laplacian);
    controls.laplacian();
  };
  laplacian.add(controls, 'laplacianSize', 1, 19, 1).name('kernel size').onChange(function(value) { if (value % 2 === 0) controls.laplacianSize = value + 1;});

  
  let contours = gui.addFolder(filters['contours']);
  contours.domElement.onclick = function() {
    closeLastFolder(contours);
    controls.contours();
  };
  
  let histograms = gui.addFolder('Histograms');
  histograms.add(controls, 'calcHist').name(filters['calcHist']).onChange(function() {
    closeLastFolder(null);
  })
  histograms.add(controls, 'equalizeHist').name(filters['equalizeHist']).onChange(function() {
    closeLastFolder(null);
  });
  
  let backprojection = histograms.addFolder(filters['backprojection']);
  backprojection.domElement.onclick = function() {
    closeLastFolder(backprojection);
    controls.backprojection();
  };
  backprojection.add(controls, 'backprojectionRangeLow', 0, 255, 1).name('range low');
  backprojection.add(controls, 'backprojectionRangeHigh', 0, 255, 1).name('range high');
}

function opencvIsReady() {
  console.log('OpenCV.js is ready');
  initUI();
  startCamera();
}