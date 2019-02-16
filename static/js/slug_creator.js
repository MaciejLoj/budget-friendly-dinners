const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

const slug_creator = (val) => {
    return val.toString().toLowerCase().trim()
        .replace(/&/g,'-and-')
        .replace(/[\s\W-]+/g,'-')

};


titleInput.addEventListener('keyup',(e)=> {
    slugInput.setAttribute('value',slug_creator(titleInput.value));


});