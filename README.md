<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>AI/ML Learning Repo</title>
  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>
  <style>
    body, html {
      margin: 0;
      padding: 0;
      scroll-behavior: smooth;
      overflow-x: hidden;
      font-family: 'Segoe UI', sans-serif;
    }
    #particles-js {
      position: fixed;
      width: 100%;
      height: 100%;
      background: #1e293b;
      z-index: -1;
    }
    pre {
      background: #f3f4f6;
      padding: 1rem;
      border-radius: 8px;
      overflow-x: auto;
    }
  </style>
</head>
<body class="text-gray-200">

<!-- Particle Background -->
<div id="particles-js"></div>

<!-- Container -->
<div class="relative z-10 max-w-3xl mx-auto py-16 px-4">

  <h1 class="text-4xl font-bold text-blue-300 mb-6 text-center">🚀 AI/ML Learning Repository</h1>
  
  <p class="text-lg mb-6 leading-relaxed text-gray-300">
    This repository is focused on hands-on learning of Artificial Intelligence (AI) and Machine Learning (ML) using Python.
    It includes step-by-step tutorials, projects, and notebooks covering core libraries like <code>numpy</code>, <code>pandas</code>, <code>matplotlib</code>,
    and <code>scikit-learn</code>. Ideal for beginners, college students, or developers looking to get into the world of data science.
  </p>

  <h2 class="text-2xl font-semibold text-blue-200 mt-8 mb-3">🔧 Technologies Covered</h2>
  <ul class="list-disc list-inside text-gray-200">
    <li>Python 3</li>
    <li>NumPy for numerical computation</li>
    <li>Pandas for data analysis</li>
    <li>Matplotlib & Seaborn for data visualization</li>
    <li>Scikit-learn for machine learning algorithms</li>
    <li>Jupyter Notebook for interactive coding</li>
  </ul>

  <h2 class="text-2xl font-semibold text-blue-200 mt-8 mb-3">📦 Install Requirements</h2>
  <div class="relative mb-6">
    <button onclick="copyCode()" class="absolute top-2 right-2 bg-blue-600 text-white text-sm px-3 py-1 rounded hover:bg-blue-700">
      Copy
    </button>
    <pre id="code-block"><code>pip install numpy pandas matplotlib scikit-learn jupyter</code></pre>
  </div>

  <h2 class="text-2xl font-semibold text-blue-200 mt-8 mb-3">📁 What You'll Learn</h2>
  <ul class="list-disc list-inside text-gray-200 space-y-1">
    <li>Data preprocessing and exploration</li>
    <li>Data visualization techniques</li>
    <li>Supervised and unsupervised learning</li>
    <li>Model training, validation, and evaluation</li>
    <li>Building AI projects from scratch</li>
  </ul>

  <h2 class="text-2xl font-semibold text-blue-200 mt-8 mb-3">🧠 Who is this for?</h2>
  <ul class="list-disc list-inside text-gray-200 space-y-1">
    <li>Beginners with no ML background</li>
    <li>B.Tech / BSc students learning AI/ML</li>
    <li>Hobbyists and self-taught learners</li>
    <li>Anyone who wants to become a Data Scientist</li>
  </ul>

  <h2 class="text-2xl font-semibold text-blue-200 mt-8 mb-3">🔗 GitHub Link</h2>
  <p><a href="https://github.com/yourusername/ai-ml-learn" class="text-blue-400 hover:underline">github.com/yourusername/ai-ml-learn</a></p>

</div>

<!-- Copy Button Script -->
<script>
  function copyCode() {
    const code = document.querySelector("#code-block code").innerText;
    navigator.clipboard.writeText(code).then(() => {
      alert("✅ Copied to clipboard!");
    }).catch(err => {
      alert("❌ Failed to copy!");
    });
  }
</script>

<!-- Particles JS Config -->
<script>
particlesJS("particles-js", {
  "particles": {
    "number": {
      "value": 60,
      "density": { "enable": true, "value_area": 800 }
    },
    "color": { "value": "#60a5fa" },
    "shape": { "type": "circle" },
    "opacity": {
      "value": 0.5,
      "random": true
    },
    "size": {
      "value": 3,
      "random": true
    },
    "line_linked": {
      "enable": true,
      "distance": 150,
      "color": "#93c5fd",
      "opacity": 0.4,
      "width": 1
    },
    "move": {
      "enable": true,
      "speed": 1,
      "direction": "none",
      "out_mode": "bounce"
    }
  },
  "interactivity": {
    "detect_on": "canvas",
    "events": {
      "onhover": { "enable": true, "mode": "grab" },
      "onclick": { "enable": true, "mode": "push" }
    },
    "modes": {
      "grab": {
        "distance": 140,
        "line_linked": { "opacity": 1 }
      }
    }
  },
  "retina_detect": true
});
</script>

</body>
</html>
