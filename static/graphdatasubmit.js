


// Asynchronous submit of form data where the object, formData is a dictionary with keys of the names of each
// form input element
function processGraphData(){
    let url = "/calculate_linear_graphs";
    let formObj = document.getElementById("mainForm");
    let formData = new FormData(formObj); // this refers to the form
    postGraphRequest(url, formData)
        .then(responseData => displayLinearGraphsHTML(responseData))
        .catch(error => console.error(error))
}
function postGraphRequest(url, formData){
    return fetch(url, {
            method: 'POST',
            body: formData
          })
          .then((response) => response.text()
          );
}
function displayLinearGraphsHTML(responseHTML){
    //console.log("responseHTML: " + responseHTML);
    let linearGraphDivObj = document.getElementById("graphContainer");
    linearGraphDivObj.innerHTML = responseHTML;
}