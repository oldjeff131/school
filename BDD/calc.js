function check()
{
    var text
    text=document.getElementById("Mun").value;
    for(let i = 0; i < text.length; i++)
    {
        if (!"1234567890+-*/() ".includes(text[i])) 
        {
            document.getElementById('anstext').value="Invalid Input";
        }
    }
    try
    {
        document.getElementById('anstext').value=eval(text);
    }
    catch(e)
    {
        document.getElementById('anstext').value="Invalid Input";
    }
}
