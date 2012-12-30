function onLyricsLoad(lyr){
	lyricsStr= lyr;	
	punctuation=false;
	lyrics_showing= true;
	$("#punctuation_checkbox").change(function(){
		if(this.checked)
			punctuation=true;
		else
			punctuation=false;	
		reprintLyrics();
	})
	
	$("#pregame").modal();
	line_num=0;
	reprintLyrics();	
	$("#nolyrics_checkbox").change(function(){
		if(this.checked)
		{
			$(".lyric_text").hide();
			lyrics_showing=false;
		}				
		else
		{
			$(".lyric_text").show();
			lyrics_showing= true;
		}				
	})		
	score=0;
	$('#pregame').on('hide', function () {
		player.playVideo();			
		reprintLyrics();
		$("#lyric_input").focus();
			
	})
	coin_sound= document.getElementById('coin_sound');
	coin_sound.volume= 0.2;
}
function reprintLyrics(){
	if(punctuation){
			lyrics= lyricsStr;
		}
	else{
		lyrics= formatLyrics(lyricsStr);				
	}
	lyrics=lyrics.split("|");
	$line1=$("#line1");
	$line2=$("#line2");
	$line3=$("#line3");
	if(line_num===0){
		$(".line").removeClass("current");
		$line1.html(lyrics[line_num]).addClass("current");
		if(line_num+1<lyrics.length)
			$line2.html(lyrics[line_num+1]);
		if(line_num+2<lyrics.length)
			$line3.html(lyrics[line_num+2]);
	}
	else if(line_num>=lyrics.length-1){
		$(".line").removeClass("current");
		$line3.html(lyrics[line_num]).addClass("current");
		if(line_num-1<lyrics.length)
			$line2.html(lyrics[line_num-1]);
		if(line_num-2<lyrics.length)
			$line1.html(lyrics[line_num-2]);
	}
	else{
		$(".line").removeClass("current");
		$line2.html(lyrics[line_num]).addClass("current");
		if(line_num-1<lyrics.length)
			$line1.html(lyrics[line_num-1]);
		if(line_num+1<lyrics.length)
			$line3.html(lyrics[line_num+1]);
	}
}
function checkInput(e, afterInput){
	$a=$("#lyric_input");
	b=lyrics[line_num];
	var same_length= $a.val().length===b.length;
	var enter_pressed= e.keyCode == 13;
	if((lyrics_showing&&enter_pressed)||(!lyrics_showing&&same_length)){
		//http://andrew.hedges.name/experiments/levenshtein/
		coin_sound.load();
		coin_sound.play();
		var points=b.length-levenshteinenator($a.val(),b);
		$a.val("");		
		score+=points;
		afterInput(points);		
	}
}
function afterInputTraining(points){
	$plus_pts= $("#player_stats .plus_points");
	$plus_pts.fadeIn('slow');
	$plus_pts.fadeOut('slow');
	$plus_pts.html("+"+points+" points");
	$("#player_stats .score h3").html(score);
	if(line_num<lyrics.length)
		line_num+=1;
	reprintLyrics();
	$("#player_stats .accuracy h3").html(calculateAccuracy()+"%");
}
function formatLyrics(lyr){
	return removePunctuation(lyr).toLowerCase();
}
function removePunctuation(str){
	var punc= ['.',',','!','?','&#39;','-', "'"];
	for (var i=0;i<punc.length;i++){
		var ch= punc[i];
		while(str.indexOf(ch)>=0)
			str=str.replace(ch,'');
	}
	return str;
}
function calculateAccuracy(){
	var chars=0;
	for(var i=0;i<line_num;i++){
		chars+=formatLyrics(lyrics[i]).length;
	}
	return Math.round(score/chars*100*100)/100;
}
function refreshModal(){		
	var accuracy= calculateAccuracy();
	$("#accuracy_pts").html(accuracy+"%");
	$("#accuracy_bar .bar").css("width", accuracy+"%");
}
