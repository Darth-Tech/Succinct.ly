document.getElementById("mybutton").addEventListener("click", GetURL);
function GetURL()
{
    // alert(`The URL of this page is:${window.location.href}`);
    chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
        let url = tabs[0].url;
        getUsers(url)
    })
}
const baseURL = "http://localhost:5000/textSummarizer?url="
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
        var myWindow = window.open("", "Succinct Summary", );
        myWindow.focus();
        myWindow.document.write('<img src="popup_icon.png" alt="Succinct.ly" style="width:200px;height:160px;" class="center"></img>');
        myWindow.document.write("<h1>Summary</h1>");
          for (const key in response.linkless) {
            myWindow.document.write("<h2>"+response.linkless[key][0]+"</h2>")
            myWindow.document.write("<p>"+response.linkless[key][1]+"</p>");
          }


    })
    .catch(err => alert(err))

  }
