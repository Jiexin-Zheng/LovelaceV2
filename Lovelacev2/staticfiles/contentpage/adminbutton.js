

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

function EditToggle(index) {	
    console.log(index)
    var currentelement = document.getElementById("formforcontent");
    console.log(currentelement.innerHTML)
	if(currentelement.style.display === "none"){
	    currentelement.style.display = "initial";		
		document.getElementById("id_index_input").value = index
		document.getElementById("id_image_index").value = index
	}
    else {
		currentelement.style.display = "none";	
		
	}
}

function DeleteContent(index) {	
    document.getElementById("id_IndexToBeDeleted").value = index
    console.log(index)
	document.getElementById("DeletionForm").submit();
}

function FormForContentToggle(id){
    console.log(id)
    var listoftogglecontent = ["textform", "imageform"];
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