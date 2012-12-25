function strcmp(a,b){
	if(a.length===b.length){
		var diff=0;
		for(var i=0;i<a.length;i++){
			if(a[i]!==b[i])
				diff+=1;
		}
		return a.length-diff;
	}
	else{
		return a.length-Math.abs(a.length-b.length);
	}
}