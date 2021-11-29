const fileInput = document.getElementById('file-input')
const fileName = document.getElementById('file-name')
var windowObjectReference;
var windowFeatures = "popup";

fileInput.addEventListener('change', evt => {
  const fileToUpload = evt.target.files[0].name
  if(fileToUpload) {
    fileName.innerText = fileToUpload
  } else {
    fileName.innerText = ""
  }
})


const instagram_url = document.getElementById("instagram_id")

instagram_url.addEventListener('click',evt =>{
  let handle = instagram_url.value

  if(handle.charAt(0)=== '@'){
    console.log("HELLOWOWOWOOWOWO")
    handle=handle.slice(1)
  }
  windowObjectReference = window.open(`https://www.instagram.com/${handle}`, "Insta_WindowName",  "left=150,top=150,width=320,height=320");
}

)

