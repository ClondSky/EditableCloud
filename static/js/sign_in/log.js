function log(){
	if($("#username")[0].value == ''){
		window.alert('请输入邮箱！');
		
	}
	else if($("#password")[0].value=='')
	{
		window.alert('请输入密码！');
	}
	else{
		$.ajax(
			{
				url:"/login",
				async:true,
				type:"POST",
				data:{
					"email":$("#username")[0].value,
					"password":$("#password")[0].value
				},
				success:function(result){
				    var ResultMessage=eval("("+result+")").ResultMessage//解析并获取json数据，此处json数据格式为{ResultMessage:Wrong}
					alert(ResultMessage);
				},
				error:function(){
					alert("服务器错误");
				}
			}
		)
	}
}

