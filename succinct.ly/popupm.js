document.getElementById("mybutton").addEventListener("click", GetURL);
function GetURL()
{   
    // alert(`The URL of this page is:${window.location.href}`);
    chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
        let url = tabs[0].url;
        getUsers(url)
    })
}
const baseURL = "http://localhost/api/v1/textSummarizer?url="
async function getUsers(param) {
    
    fetch(
      baseURL.concat(param) , {
      method: 'GET',
      
      headers : { 
        'accept': 'application/json'
       },
       
      }
    ).then(response => response.json())
    .then((response) => {
        var myWindow = window.open("", "", );
        myWindow.focus();
        myWindow.document.write("<h1>Summary</h1>");
        myWindow.document.write("<h1>"+response.linkless+"</h1>");
    })
    .catch(err => alert(err))
    
  }