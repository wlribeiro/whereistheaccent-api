var atualWord = {};
var wordList = [];

// document.getElementById('#verify').addEventListener('keypress', function ( event ) {
//     console.log('iam here')
//     if (event.key === 'Enter') {
//         verifyWirite()
//     }
// });

(async ()=>
    {
        const url = window.location.href;;
        const endpoint = "v1/words/accented";

        const response = await fetch( url + endpoint );
        if( response.status !== 200 )
        {
            console.log( "something happened" );
        }

        const data = ( await response.json() );
        shuffleWords(data);
        wordList = [...data];
        renderWord()
    }
)();

function shuffleWords(wordList) 
{
    for (let i = wordList.length - 1; i > 0; i--) 
    {
        const j = Math.floor(Math.random() * (i + 1));
        [wordList[i], wordList[j]] = [wordList[j], wordList[i]];
    }
}

function verifyWirite ( value ) 
{
    if ( !value?.event.key === "Enter" ) { return }
    const wordContainer = document.querySelector( "#word" );
    if ( atualWord.word.toUpperCase() === wordContainer.value.toUpperCase() )
    {
        renderWord();
        wordContainer.value = "";
    }
}

function renderWord () 
{
    atualWord = wordList.pop(0);
    atualWord[ "wordWithoutAccents" ] = removeAccents( atualWord.word );
    document.querySelector( "#peek" ).value = capitalize(atualWord.wordWithoutAccents);
}

function removeAccents (str) 
{
    return str.normalize( "NFD" ).replace( /[\u0300-\u036f]/g, "" );
}

function capitalize (str)
{
    return str.charAt(0).toUpperCase() + str.slice(1)
}
