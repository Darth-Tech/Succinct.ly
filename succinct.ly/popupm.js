document.getElementById("mybutton").addEventListener("click", GetURL);
function GetURL()
{
    // alert(`The URL of this page is:${window.location.href}`);
    chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
        let url = tabs[0].url;
        alert("The URL of this page is: " + url);// use `url` here inside the callback because it's asynchronous!
    });
}
    
   