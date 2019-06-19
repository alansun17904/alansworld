(function() {
    // Reset all checkboxes
    $("#selectall").on("click", function() {
        // display a nice message if nothing is selected
        $("#nonselected").get(0).style["display"] = this.checked ? "none": "block";
        for (otherTags of $(".filter input:first-child")) {
            otherTags.checked = this.checked
        }
        for (question of $(".thought")) {
            question.style["display"] = this.checked ? "block": "none";
        }
    })

    for (filter of $(".filter input:first-child")) {
        filter.addEventListener("click", function() {
            tagName = this.id
            console.log(tagName)
            for (tag of $(".thought").find("span")) {
                console.log(tag.textContent)
                if (tag.textContent == tagName) {
                    console.log("HIIII")
                    tag.parentNode.parentNode.style["display"] = this.checked ? "block": "none";
                }
            }
        })
    }
    $("#selectall").checked = true;
})()
