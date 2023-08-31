
function shaft = create_shaft(collision_geometries, dh_params)
    shaft = rigidBodyTree("DataFormat", "column");
    basename=shaft.BaseName;
    
    cylinder_1 = rigidBody('cylinder_1');
    cylinder_2 = rigidBody('cylinder_2');
    %cylinder_3 = rigidBody('cylinder_3');
    cylinder_4 = rigidBody('cylinder_4');
    cylinder_5 = rigidBody('cylinder_5');
    cylinder_6 = rigidBody('cylinder_6');
    cylinder_7 = rigidBody('cylinder_7');
    cylinder_8 = rigidBody('cylinder_8');
    
    joint_1 = rigidBodyJoint('joint_1','revolute');
    joint_1.JointAxis=[0,1,0];
    cylinder_1.Joint=joint_1;
    setFixedTransform(joint_1,dh_params(1,:),'dh');
    
    joint_2 = rigidBodyJoint('joint_2','fixed');
    setFixedTransform(joint_2,dh_params(2,:),'dh');
    cylinder_2.Joint=joint_2;
    
%     joint_3 = rigidBodyJoint('joint_3','fixed');
%     setFixedTransform(joint_3,dh_params(3,:),'dh');
%     cylinder_3.Joint=joint_3;
    
    joint_4 = rigidBodyJoint('joint_4','fixed');
    setFixedTransform(joint_4,dh_params(4,:),'dh');
    cylinder_4.Joint=joint_4;
    
    joint_5 = rigidBodyJoint('joint_5','fixed');
    setFixedTransform(joint_5,dh_params(5,:),'dh');
    cylinder_5.Joint=joint_5;
    
    joint_6 = rigidBodyJoint('joint_6','fixed');
    setFixedTransform(joint_6,dh_params(6,:),'dh');
    cylinder_6.Joint=joint_6;
    
    joint_7 = rigidBodyJoint('joint_7','fixed');
    setFixedTransform(joint_7,dh_params(7,:),'dh');
    cylinder_7.Joint=joint_7;
    
    joint_8 = rigidBodyJoint('joint_8','fixed');
    setFixedTransform(joint_8,dh_params(8,:),'dh');
    cylinder_8.Joint=joint_8;
    
    addBody(shaft, cylinder_1, basename);
    addBody(shaft, cylinder_2, 'cylinder_1');
    %addBody(shaft, cylinder_3, 'cylinder_2');
    addBody(shaft, cylinder_4, 'cylinder_2');
    addBody(shaft, cylinder_5, 'cylinder_4');
    addBody(shaft, cylinder_6, 'cylinder_5');
    addBody(shaft, cylinder_7, 'cylinder_6');
    addBody(shaft, cylinder_8, 'cylinder_7');
    

    for i=1:length(collision_geometries)
        cylinder = collision_geometries{i};
        collision_cylinder = collisionCylinder(cylinder.radius, cylinder.length);
        axis = [0 1 0 pi/2];
        transformation = trvec2tform([cylinder.length/2,0,0])*axang2tform(axis);
        collision_cylinder.Pose = transformation;
        addCollision(shaft.Bodies{i}, collision_cylinder);
    end
    