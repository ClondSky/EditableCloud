function log(){
	
	if($(“#username”)[0].value == ''){
		window.alert('请输入邮箱！')
		
	}
	else if($(“#password”)[0].value==''){
		window.alert('请输入密码！')
	}
	else{
		$.ajax(
		{
			url:'/login',
			type:'POST', //GET
			async:true,    //或false,是否异步
			data:{
				"email":$(“#username”)[0].value,
				"password":$(“#password”)[0].value
			},
			dataType:'json',    //返回的数据格式：json/xml/html/script/jsonp/text
			beforeSend:function(xhr){
				console.log(xhr)
				console.log('发送前')
			},
			success:function(data,textStatus,jqXHR){
				console.log(data)
				console.log(textStatus)
				console.log(jqXHR)
			},
			error:function(xhr,textStatus){
				console.log('错误')
				console.log(xhr)
				console.log(textStatus)
			},
			complete:function(){
				console.log('结束')
		}
		)
	}
}

