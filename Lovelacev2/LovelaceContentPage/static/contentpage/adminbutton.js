

function AdminToggle() {	
    var currentelement = document.getElementById("adminOnly");
    var adminelements = document.querySelectorAll(".pieceofcontent-admin,.slotforcontent");
    console.log(currentelement)
	if(currentelement.style.display === 'none'){
	    for(var i = 0; i<adminelements.length; i++){
			adminelements[i].style.display = "flex";
			console.log(adminelements[i].style.display)
		}
	}
    else {
		for(var i = 0; i<adminelements.length; i++){
			adminelements[i].style.display = "none";
	}
	}
}
//AdminToggle handles opening and closing the editing options


function EditToggle(index) {	
    console.log(index)
    var currentelement = document.getElementById("formforcontent");
    console.log(currentelement.innerHTML)
	if(currentelement.style.display === "none"){
	    currentelement.style.display = "initial";		
		document.getElementById("id_index_input").value = index
		document.getElementById("id_image_index").value = index
		document.getElementById("id_file_index").value = index
		document.getElementById("id_exercise_index").value = index
		document.getElementById("id_EditMode").value = "False"
		document.getElementById("id_EditModeImage").value = "False"
		document.getElementById("id_EditModeFile").value = "False"
		document.getElementById("id_EditModeExercise").value = "False"
	}
    else {
		currentelement.style.display = "none";	
		
	}
}

var ContextArray = [];

function Showandhide(ContextArray) {
	var Value = document.getElementById("id_file").value 
	if(ContextArray.length > 1){
		ContextArray.shift();
	}
	ContextArray.push(Value)
	document.getElementById(ContextArray[0]).style.display = "none"
	document.getElementById(ContextArray[1]).style.display = "initial"
}


//edittoggle opens the popup with the image and text forms
function DeleteContent(index) {	
    document.getElementById("id_IndexToBeDeleted").value = index
    console.log(index)
	document.getElementById("DeletionForm").submit();
}
//DeleteContent is function that is run when the - sign is pressed. The index parameter gets the value from the html template's for loop. It gets then passed to the deletion form and the deletion form gets automatically submitted by this function, the user doesnt fill anything on the form.

function EditContent(index, ContentArray) {	
    var ContentToBeEdited = ContentArray[index];
    console.log(ContentToBeEdited[4])
    var currentelement = document.getElementById("formforcontent");
	if(currentelement.style.display === "none"){
		if(ContentToBeEdited[0] ===  "Text"){
			document.getElementById("textform").style.display = "initial";
			document.getElementById("imageform").style.display = "none";
			document.getElementById("fileform").style.display = "none";
		}
		if(ContentToBeEdited[0] ===  "Image"){
			document.getElementById("imageform").style.display = "initial";
			document.getElementById("textform").style.display = "none";
			document.getElementById("fileform").style.display = "none";
		}
		if(ContentToBeEdited[0] ===  "EmbeddedExercise"){
			document.getElementById("imageform").style.display = "none";
			document.getElementById("textform").style.display = "none";
			document.getElementById("exampleexerciseform").style.display = "initial";
		}

	    currentelement.style.display = "initial";		
	    document.getElementsByClassName("formforcontentheader")[0].innerHTML = "Edit the selected content.";
		document.getElementById("id_index_input").value = index
		document.getElementById("id_image_index").value = index
		document.getElementById("id_exercise_index").value = index
		document.getElementById("id_text_input").value = ContentToBeEdited[1]
		document.getElementById("id_header_input").value = ContentToBeEdited[2]
		document.getElementById("id_imagetitle").value = ContentToBeEdited[3]
		document.getElementById("id_imagecaption").value = ContentToBeEdited[4]
		document.getElementById("id_exercisetext").value = ContentToBeEdited[6]
		document.getElementById("id_exercisetype").value = ContentToBeEdited[7]
		document.getElementById("id_EditMode").value = "True"
		document.getElementById("id_EditModeImage").value = "True"
		document.getElementById("id_EditModeFile").value = "True"
		document.getElementById("id_EditModeExercise").value = "True"

	}
    else {
		currentelement.style.display = "none";	
		document.getElementsByClassName("formforcontentheader")[0].innerHTML = "Add content to the selected position.";
        document.getElementById("textform").style.display = "none";
        document.getElementById("imageform").style.display = "none";
        document.getElementById("fileform").style.display = "none";
        document.getElementById("exampleexerciseform").style.display = "none";
        document.getElementById("id_text_input").value = ""
		document.getElementById("id_header_input").value = ""
		document.getElementById("id_imagetitle").value = ""
		document.getElementById("id_imagecaption").value = ""
        document.getElementById("id_EditMode").value = "False"
		document.getElementById("id_EditModeImage").value = "False"
		document.getElementById("id_EditModeFile").value = "False"
		document.getElementById("id_EditModeExercise").value = "False"
		document.getElementById("id_exercisetext").value = ""
		document.getElementById("id_exercisetype").value = ""
}
}

function FormForContentToggle(id){
    console.log(id)
    var listoftogglecontent = ["textform", "imageform", "fileform", "exampleexerciseform"];
    var length = listoftogglecontent.length;
	for (var i = 0; i < length; i++) {
	    if(listoftogglecontent[i] == id.id){
			document.getElementById(id.id).style.display = "initial";
		}
		else{
			document.getElementById(listoftogglecontent[i]).style.display = "none";
		}
    }
}
//FormForContentToggle is for toggling between image and text forms in the FormForContent in html. if new content types is added, the listoftogglecontent variable should have the new contenttype added to the list.