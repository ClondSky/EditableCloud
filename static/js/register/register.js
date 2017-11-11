function register(){
	if($("#username")[0].value == ''){
		window.alert('请输入邮箱！');
		
	}
	else if($("#password")[0].value=='')
	{
		window.alert('请输入密码！');
		
	}
	else if($("#againpassword")[0].value=='')
	{
		window.alert('请再次输入密码！');
		
	}
	else if($("#againpassword")[0].value!=$("#password")[0].value)
	{
		window.alert('请输入相同密码！');

	}
	else if($("#name")[0].value=='')
	{
		window.alert('请输入您的姓名！');

	}
	else{
		$.ajax(
			{
				url:"/register",
				async:true,
				type:"POST",
				data:{
					"email":$("#username")[0].value,
					"password":$("#password")[0].value,
					"name":$("#name")[0].value
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