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
					"username":$("#username")[0].value,
					"password":$("#password")[0].value
				},
				success:function(result){
					alert("登录成功");
				},
				error:function(){
					alert("服务器错误");
				}
			}
		)
	}
}

