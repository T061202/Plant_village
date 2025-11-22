* {
    margin: 0;
    padding: 0;
    font-family: "Segoe UI", sans-serif;
    box-sizing: border-box;
}

body {
    background: linear-gradient(135deg, #d7ffd9, #b2fab4);
}


.hero {
    height: 250px;
    background: url('https://images.unsplash.com/photo-1495202337139-570158a5f6f1?auto=format&fit=crop&w=1350&q=80') center/cover no-repeat;
    display: flex;
    align-items: center;
    justify-content: center;
    backdrop-filter: blur(6px);
}

.hero-content {
    background: rgba(255, 255, 255, 0.35);
    padding: 25px 40px;
    border-radius: 20px;
    text-align: center;
    backdrop-filter: blur(10px);
}

.hero h1 {
    font-size: 32px;
    font-weight: 800;
    color: #0b3d0b;
}

.hero p {
    margin-top: 10px;
    color: #1e4620;
    font-size: 16px;
}


.container {
    margin-top: -50px;
    display: flex;
    justify-content: center;
    padding: 30px;
}

.upload-card {
    width: 450px;
    padding: 25px;
    background: white;
    border-radius: 20px;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.12);
    text-align: center;
}

.upload-card h2 {
    margin-bottom: 20px;
    color: #1b5e20;
}


.upload-area {
    width: 100%;
    height: 160px;
    border: 2px dashed #4caf50;
    border-radius: 15px;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    color: #388e3c;
    font-size: 18px;
    transition: 0.3s;
}

.upload-area:hover {
    background: #e8f5e9;
}


.preview {
    width: 100%;
    margin-top: 15px;
    border-radius: 15px;
}


.btn {
    margin-top: 15px;
    padding: 12px 20px;
    width: 100%;
    border: none;
    border-radius: 15px;
    background: #2e7d32;
    color: white;
    font-size: 18px;
    cursor: pointer;
    transition: 0.2s;
}

.btn:disabled {
    background: gray;
    cursor: not-allowed;
}

.btn:hover:not(:disabled) {
    background: #1b5e20;
}


.loading {
    margin-top: 20px;
}

.spinner {
    width: 40px;
    height: 40px;
    border: 5px solid #c8e6c9;
    border-top-color: #2e7d32;
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
    margin: auto;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

.result-card {
    margin-top: 20px;
    padding: 20px;
    background: #f1f8e9;
    border-left: 6px solid #4caf50;
    border-radius: 10px;
    animation: fadeIn 0.4s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
.camera-box {
    margin-top: 15px;
    position: relative;
}

#cameraStream {
    width: 100%;
    border-radius: 15px;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.15);
}

.capture {
    background: #1565c0;
    margin-top: 10px;
}

.capture:hover {
    background: #0d47a1;
}
