
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    console.log(sender.tab ?
                "from a content script:" + sender.tab.url :
                "from the extension");
    document.getElementById("summary").innerHTML = request.greeting;
  });
  chrome.runtime.onMessage.addListener((message, sender, sendResponse)=> {
      document.getElementById("summary").innerHTML = message;
// do what you want to the message
      console.log(message);
  });

