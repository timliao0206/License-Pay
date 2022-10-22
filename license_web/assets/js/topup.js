function insc() {
    var count = document.getElementById("count").innerHTML;
    document.getElementById("count").innerHTML = parseInt(count) + 50;
    }
    function dec() {
        var count=document.getElementById("count").innerHTML;
        if(parseInt(count) > 50 ){
            document.getElementById("count").innerHTML = parseInt(count) - 50;		
        };
    }