//nav.js
Parse.initialize("ZyuBO9FvD4ck1jdDcDjfx8c0ktptHeid7kn07SMt", "WyXKhdQ7z34qsz2QacMVjpiTIPEr037OwIfW2PPy");
if (Parse.User.current() !== null){
	var currentUserId = Parse.User.current().id;
	var currentUser = Parse.User.current();
}else{
	//Redirect Out
	window.location.href = 'index.html';
}

var xmlhttp;
var where;
var type;
var postid;

$(document).keydown(function (e) {
  if (e.keyCode == 66) {
    window.history.back();
  }
});

//URL Checker
function isUrl(s) {
   var regexp = /(ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/
   return regexp.test(s);
}

function formatURL(url){

	//Format URL before it's finished saving for website
	//TODO: Check to make sure this works with https://site.com

	var urlFormatted;
	if (url.indexOf('www.') > -1) { url = url.split('www.')[1]; }
	urlFormatted = "http://www." + url;
	return urlFormatted;
}

function toTitleCase(str){
	return str.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
}


function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

//Ranking Recent Posts
function convertSeconds(date){
	var seconds = date.getTime() / 1000;
	return seconds;
}

//AJAX Navigations

//Ajax Callback
//Location is passed to.
function Ajax(where, type){

	window.history.pushState(type, null, null); //state, title, url to display
	$.ajax({url: where, 
		success: function(result){
        	$("#content_container").html(result);
    	}	
    });
}

//Feed
function showFeed(){
	$('.nav_buttons li').css('background-color', "");
	Ajax("feed.html");
	//$("#search_input").val("");
}

//Search
function search(){
	var searching_for = $('#search_input').val();
	if (searching_for.length > 0){
		Ajax("search.html", searching_for);
	}
}

//Messenger
function showMessenger(){
	$('.nav_buttons li').css('background-color', "");
	$('#nav_messenger').css('background-color', '#f5f5f5');
	Ajax("client.html");
}

//Directory
function showDirectory(){
	$('.nav_buttons li').css('background-color', "");
	$('#nav_peers').css('background-color', '#f5f5f5');
	Ajax("directory.html");
}

//Calendar
function showCalendar(){
	$('.nav_buttons li').css('background-color', "");
	$('#nav_cal').css('background-color', '#f5f5f5');
	Ajax("calendar.html");
}

//Profile
function showProfile(){
	$('.nav_buttons li').css('background-color', "");
	$('#nav_you').css('background-color', '#f5f5f5');
	Ajax("profile.html", currentUserId);
}

//Reservations
function showRoomReservations(){
	$('.nav_buttons li').css('background-color', "");
	$('#nav_rooms').css('background-color', '#f5f5f5');
	Ajax("reserve.html");
}

//Resources Post
function postResource(){
	$('.nav_buttons li').css('background-color', "");
	$('#nav_resource').css('background-color', 'rgba(0, 196, 0, 0.1)');
	Ajax("new.html", "Resource");
}

function goToPost(postid){
	$('.nav_buttons li').css('background-color', "");
	Ajax("post.html", postid);
}

//Company Profile
function goToCompany(companyId){
	$('.nav_buttons li').css('background-color', "");
	Ajax("profile_company.html", companyId);
}

//Event Post
function postEvent(){
	$('.nav_buttons li').css('background-color', "");
	$('#nav_event').css('background-color', 'rgba(245, 0, 0, 0.1)');
	Ajax("new.html", "Event");
}

//Question Post
function postQuestion(){
	$('.nav_buttons li').css('background-color', "");
	$('#nav_question').css('background-color', 'rgba(245, 180, 0, 0.1)');
	Ajax("new.html", "Question");
}

//Job Post
function postJob(){
	$('.nav_buttons li').css('background-color', "");
	$('#nav_job').css('background-color', 'rgba(0,12,170, 0.1)');
	Ajax("new.html", "Job");
}

//As this is the landing page, feed should automatically load.
$(document).ready(showFeed());
