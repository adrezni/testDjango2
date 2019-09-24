let fileChooserObj = document.getElementById("filechooser");
let uploadButtonObj = document.getElementById("uploadCSV");
let msgDivObj = document.getElementById("msgDivFileUpload");

fileChooserObj.addEventListener('change', handleFileSelect, false);
/*
    Once file has been selected, enable the Upload CSV button.
 */
function handleFileSelect(){
    uploadButtonObj.disabled = false;
}
/*
This is an asynchronous post that calls upon the endpoint, '/uploadCSV'.  That action uploads the CSV file to
the server, creates a dataframe from the CSV file and stores it in the session.
 */
function uploadCSVAction(){
    let url = '/uploadCSV';
    uploadButtonObj.disabled = true;
    msgDivObj.innerHTML = "Uploading .....";
    let csvFile = fileChooserObj.files[0];
    // FormData is a dictionary that allows key-value pairs to be put into one object
    let formData = new FormData;
    // Put a key-value pair into the FormData object.  Key = "filechooser", value = csvFile
    formData.append("filechooser", csvFile, csvFile.name);

    postRequest(url, formData)
        .then(responseText => displayResponseHTML(responseText))
        .catch(error => console.error(error))
}
/*
    Posts a FormData request to the given url.  The formData param is a FormData object
    The response value is a text string which is a success message
 */
function postRequest(url, formData) {
      return fetch(url, {
        method: 'POST',
        body: formData
      })
        .then((response) => response.text()  // response comes from server side endpoint function.
      );
}
function displayResponseHTML(responseTxt){
    msgDivObj.innerHTML = responseTxt;
    // Graphs button is initially disabled until a csv file has been uploaded.
    graphsBtnObj = document.getElementById("graphsBtn");
    graphsBtnObj.disabled = false;
}
