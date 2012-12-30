(function(){
	PUBNUB.subscribe({
        channel    : "battle",      // CONNECT TO THIS CHANNEL.

        restore    : false,              // STAY CONNECTED, EVEN WHEN BROWSER IS CLOSED
        // OR WHEN PAGE CHANGES.

        callback   : function(message) { // RECEIVED A MESSAGE.
            switch (message.name){
                case 'opponent_requested':
                    if (message.userId != Player.userId && !Player.opponentId){
                        Player.opponentId = message.userId;
                        publish('opponent_found', {opponentId: Player.userId, userId: message.userId});
                    }
                    break;

                case 'opponent_found':
                    if (message.userId == Player.userId && !Player.opponentId){
                        Player.opponentId = message.opponentId;
                        publish('fight', {userIds: [Player.userId, Player.opponentId]});
                    }
                    break;

                case 'fight':
                    $.each(message.userIds, function(i, id){
                        if (id == Player.userId){
                            alert('Get Ready to Battle!');
                        }
                    });

                case 'opponent_surrendered':
                    if (message.userId == Player.userId){
                        alert('Opponent Surrendered! You Win!');
                    }
                    break;

                case 'opponent_score':
                    if (message.userId == Player.userId){
                        grunt= document.getElementById('grunt');
                        setOpponentStats(message.opponentPoints);
                        grunt.load();
                        grunt.play();
                    }

            }
        },

        disconnect : function() {        // LOST CONNECTION.
            publish('opponent_surrendered', {opponentId: Player.userId, userId: Player.opponentId});
        },

        reconnect  : function() {        // CONNECTION RESTORED.
            alert("And we're Back!")
        },

        connect    : function() {        // CONNECTION ESTABLISHED.
            publish('opponent_requested', {userId: Player.userId});
        }
    });    
}());
function setOpponentStats(points){
	Player.opponentScore+=points;
	$plus_pts= $("#opponent_stats .plus_points");
	$plus_pts.fadeIn('slow');
	$plus_pts.fadeOut('slow');
	$plus_pts.html("+"+points+" points");
	$("#opponent_stats .score h3").html(Player.opponentScore);
	if(line_num<lyrics.length)
		line_num+=1;
	reprintLyrics();
	$("#player_stats .accuracy h3").html(calculateAccuracy()+"%");
}
function publish(event, data){
        data.name = event;

        PUBNUB.publish({             // SEND A MESSAGE.
            channel : "battle",
            message : data
        });
    }
function afterInputBattle(points){
	afterInputTraining(points);
	publish('opponent_score', {opponentId: Player.userId, userId: Player.opponentId, opponentPoints: points});
}
