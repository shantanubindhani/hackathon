<div class="col-md-6">                    
	<div class="panel panel-info" >
		<div class="panel-heading">
			<div class="panel-title">Sign In</div>                        
		</div> 
		<div style="padding-top:30px" class="panel-body" >
			<?php if ($errorMessage != '') { ?>
				<div id="login-alert" class="alert alert-danger col-sm-12"><?php echo $errorMessage; ?></div>                            
			<?php } ?>
			<form id="loginform" class="form-horizontal" role="form" method="POST" action="">                                    
				<div style="margin-bottom: 25px" class="input-group">
					<span class="input-group-addon"><i class="glyphicon glyphicon-user"></i></span>
					<input type="text" class="form-control" id="email" name="email" placeholder="email">                                
				</div>                                
				<div style="margin-bottom: 25px" class="input-group">
					<span class="input-group-addon"><i class="glyphicon glyphicon-lock"></i></span>
					<input type="password" class="form-control" id="loginPass" name="loginPass" placeholder="password">
				</div>            
				<div style="margin-top:10px" class="form-group">                               
					<div class="col-sm-12 controls">
					  <input type="submit" name="login" value="Login" class="btn btn-success">						  
					</div>
				</div>                                
			</form>   
		</div>                     
	</div>  
</div>