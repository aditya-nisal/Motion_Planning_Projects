function fixed_shaft = get_fixed_shaft()
     axis = [0 1 0 pi/2];
    
    c1 = struct("len", 0.76, "rad", 0.36, "trans", [1.98; 0; -2.31;]);

    coll_shaft1 = collisionCylinder( c1.rad,c1.len);
    transformation = axang2tform(axis);
    transformation(1:3, 4) = c1.trans;
    coll_shaft1.Pose = transformation;
    fixed_shaft{1} = coll_shaft1;
%---------------------------------------------------------------------------------
    c2 = struct("len", 0.5, "rad", 1, "trans", [2.61; 0; -2.31;]);
    coll_gear1 = collisionCylinder(c2.rad, c2.len);
    axis = [0 1 0 pi/2];
    transformation = axang2tform(axis);
    transformation(1:3, 4) = c2.trans;
    coll_gear1.Pose = transformation;
    fixed_shaft{2} = coll_gear1;
%----------------------------------------------------------------------------------
    c3 = struct("len", 0.76, "rad", 0.36, "trans", [3.25; 0; -2.31;]);
    coll_shaft2 = collisionCylinder( c3.rad,c3.len);

    transformation = axang2tform(axis);
    transformation(1:3, 4) = c3.trans;
    coll_shaft2.Pose = transformation;
    fixed_shaft{3} = coll_shaft2;
% ----------------------------------------------------------------------------   
    c4 = struct("len", 0.5, "rad", 0.8, "trans", [3.87; 0; -2.31;]);
    coll_gear2 = collisionCylinder(c4.rad,c4.len);

    transformation = axang2tform(axis);
    transformation(1:3, 4) = c4.trans;
    coll_gear2.Pose = transformation;
    fixed_shaft{4} = coll_gear2;
% ------------------------------------------------------------------------------
 
    c5 = struct("len", 0.16, "rad", 0.36, "trans", [4.2; 0; -2.31;]);
    coll_shaft3 = collisionCylinder( c5.rad,c5.len);

    transformation = axang2tform(axis);
    transformation(1:3, 4) = c5.trans;
    coll_shaft3.Pose = transformation;
    fixed_shaft{5} = coll_shaft3;
% -----------------------------------------------------------------------------    
    c6 = struct("len", 0.5, "rad", 1.235, "trans", [4.51; 0; -2.31;]);
    coll_gear3 = collisionCylinder( c6.rad,c6.len);

    transformation = axang2tform(axis);
    transformation(1:3, 4) = c6.trans;
    coll_gear3.Pose = transformation;
    fixed_shaft{6} = coll_gear3;
% --------------------------------------------------------------------------------

    c7 = struct("len", 0.5, "rad", 1.395, "trans", [5.03; 0; -2.31;]);
    coll_gear4 = collisionCylinder(c7.rad, c7.len);

    transformation = axang2tform(axis);
    transformation(1:3, 4) = c7.trans;
    coll_gear4.Pose = transformation;
    fixed_shaft{7} = coll_gear4;
%-----------------------------------------------------------------------------   
    c8 = struct("len", 1.82, "rad", 0.36, "trans", [6.19; 0; -2.31;]);
    coll_shaft4 = collisionCylinder(c8.rad,c8.len );

  
    transformation = axang2tform(axis);
    transformation(1:3, 4) = c8.trans;
    coll_shaft4.Pose = transformation;
    fixed_shaft{8} = coll_shaft4;
%--------------------------------------------------------------------  
    c9 = struct("len", 0.5, "rad", 1.40, "trans", [7.35; 0; -2.31]);
    coll_gear5 = collisionCylinder(c9.rad, c9.len);

    transformation = axang2tform(axis);
    transformation(1:3, 4) = c9.trans;
    coll_gear5.Pose = transformation;
    fixed_shaft{9} = coll_gear5;
%  -------------------------------------------------------------------  
    c10 = struct("len", 0.6, "rad", 0.36, "trans", [7.9; 0; -2.31;]);
    coll_shaft5 = collisionCylinder(c10.len, c10.rad);

    transformation = axang2tform(axis);
    transformation(1:3, 4) = c10.trans;
    coll_shaft5.Pose = transformation;
    fixed_shaft{10} = coll_shaft5;
% -------------------------------------------------------------------------  

 end