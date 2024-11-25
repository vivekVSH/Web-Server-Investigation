// Handle Login
document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.getElementById("loginForm");
    const errorMessage = document.getElementById("errorMessage");
  
    if (loginForm) {
      loginForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;
  
        if (username === "admin" && password === "password123") {
          window.location.href = "investigation.html";
        } else {
          errorMessage.textContent = "Invalid username or password!";
        }
      });
    }
  
    // Handle PDF Download
    const downloadPdfButton = document.getElementById("downloadPdf");
    if (downloadPdfButton) {
      downloadPdfButton.addEventListener("click", () => {
        const analysisText = document.getElementById("analysis").value;
  
        if (!analysisText) {
          alert("Please enter some analysis before downloading the PDF.");
          return;
        }
  
        const { jsPDF } = window.jspdf;
        const doc = new jsPDF();
  
        doc.text("Web Server Investigation", 10, 10);
        doc.text(analysisText, 10, 20);
        doc.save("web-server-investigation.pdf");
      });
    }
  });
  