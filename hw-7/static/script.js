document.getElementById('clickButton').addEventListener(
    'click',
    function() {
        new_elmt = document.createElement('div')
        new_elmt.innerHTML = "You clicked me!"
        document.getElementById('display_area').appendChild(new_elmt)
    }
);