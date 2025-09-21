function showPassword(){
    const pass = document.getElementById("pass");
    const input = document.getElementById("input");
    if (input.type === "password"){
        input.type = "text";
        pass.textContent = "Hide";
    }
    else{
        input.type = "password";
        pass.textContent = "Show";
    }
}
async function checkPassword() {
      const password = document.getElementById("input").value;

      const response = await fetch("http://127.0.0.1:5000/check", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        cache:"no-store",
        body: JSON.stringify({ password: password })
      });

      const data = await response.json();
      if (data.strength ==="Weak"){
        document.getElementById("Strength").style.color = "red";
      }
      else if (data.strength ==="Medium"){
        document.getElementById("Strength").style.color = "Yellow";
      }
      else if (data.strength ==="Strong"){
        document.getElementById("Strength").style.color = "Green";
      }
      else{
        document.getElementById("Strength").style.color = "black";
      }
      document.getElementById("Strength").textContent = "Strength: "+ data.strength;
      document.getElementById("Generated").textContent = "Generated Password: "+ data.secure_password;
    }