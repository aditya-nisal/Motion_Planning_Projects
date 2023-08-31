function walls = get_walls()
    % to generate the right side of the wall
    walls = {};
    right_wall_s1 = struct("x", .5, "y", 4.2, "z", 1.7, "trans", [.25+1.6; 0; -3.95]);
    box = collisionBox(right_wall_s1.x, right_wall_s1.y, right_wall_s1.z);
    transformation = [eye(3) right_wall_s1.trans; 0 0 0 1];
    box.Pose = transformation;
    walls{1} = box;
   
    right_wall_s2 = struct("x", .5, "y", 1.3, "z", 1.6, "trans", [.25+1.6; 1.45; -2.3]);
    box = collisionBox(right_wall_s2.x, right_wall_s2.y, right_wall_s2.z);
    transformation = [eye(3) right_wall_s1.trans; 0 0 0 1];
    box.Pose = transformation;
    walls{2} = box;

    right_wall_s3 = struct("x", .5, "y", 1.3, "z", 1.6, "trans", [.25+1.6; -1.45; -2.3]);
    box = collisionBox(right_wall_s3.x, right_wall_s3.y, right_wall_s3.z);
    transformation = [eye(3) right_wall_s3.trans; 0 0 0 1];
    box.Pose = transformation;
    walls{3} = box;

    right_wall_s4 =  struct("x", .5, "y", 4.2, "z", 0.7, "origin", [.25+1.6; 0; -1.15]);
    box = collisionBox(right_wall_s4.x, right_wall_s4.y, right_wall_s4.z);
    transformation = [eye(3) right_wall_s4.origin; 0 0 0 1];
    box.Pose = transformation;
    walls{4} = box;


    right_wall_s5 = struct("x", .5, "y", 1.3, "z", 1.6, "origin", [.25+1.6; 1.45; 0]);
    box = collisionBox(right_wall_s5.x, right_wall_s5.y, right_wall_s5.z);
    transformation = [eye(3) right_wall_s4.origin; 0 0 0 1];
    box.Pose = transformation;
    walls{5} = box;

    right_wall_s6 =  struct("x", .5, "y", 1.3, "z", 1.6, "origin", [.25+1.6; -1.45; 0]);
    box = collisionBox(right_wall_s6.x, right_wall_s6.y, right_wall_s6.z);
    transformation = [eye(3) right_wall_s6.origin; 0 0 0 1];
    box.Pose = transformation;
    walls{6} = box;

    right_wall_s7 =  struct("x", .5, "y", 4.2, "z", 0.9, "origin", [.25+1.6; 0; 1.25]);
    box = collisionBox(right_wall_s7.x, right_wall_s7.y, right_wall_s7.z);
    transformation = [eye(3) right_wall_s7.origin; 0 0 0 1];
    box.Pose = transformation;
    walls{7} = box;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % to generate the left side of the wall
    left_wall_s1 = struct("x", .5, "y", 4.2, "z", 1.7, "origin", [6.35+1.6; 0; -3.9]);
    box = collisionBox(left_wall_s1.x, left_wall_s1.y, left_wall_s1.z);
    transformation = [eye(3) left_wall_s1.origin; 0 0 0 1];
    box.Pose = transformation;
    walls{8} = box;
        
    left_wall_s2 =  struct("x", .5, "y", 1.3, "z", 1.6, "origin", [6.35+1.6; 1.45; -2.3]);
    box = collisionBox(left_wall_s2.x, left_wall_s2.y, left_wall_s2.z);
    transformation = [eye(3) left_wall_s2.origin; 0 0 0 1];
    box.Pose = transformation;
    walls{9} = box;
    
    left_wall_s3 =   struct("x", .5, "y", 1.3, "z", 1.6, "origin", [6.35+1.6; -1.45; -2.3]);
    box = collisionBox(left_wall_s3.x, left_wall_s3.y, left_wall_s3.z);
    transformation = [eye(3) left_wall_s3.origin; 0 0 0 1];
    box.Pose = transformation;
    walls{10} = box;
    
    left_wall_s4 =  struct("x", .5, "y", 4.2, "z", 0.7, "origin", [6.35+1.6; 0; -1.15]);
    box = collisionBox(left_wall_s4.x, left_wall_s4.y, left_wall_s4.z);
    transformation = [eye(3) left_wall_s4.origin; 0 0 0 1];
    box.Pose = transformation;
    walls{11} = box;
    
    left_wall_s5 = struct("x", .5, "y", 1.3, "z", 1.6, "origin", [6.35+1.6; 1.45; 0]);
    box = collisionBox(left_wall_s5.x, left_wall_s5.y, left_wall_s5.z);
    transformation = [eye(3) left_wall_s5.origin; 0 0 0 1];
    box.Pose = transformation;
    walls{12} = box;
    
    left_wall_s6 =  struct("x", .5, "y", 1.3, "z", 1.6, "origin", [6.35+1.6; -1.45; 0]);
    box = collisionBox(left_wall_s6.x, left_wall_s6.y, left_wall_s6.z);
    transformation = [eye(3) left_wall_s6.origin; 0 0 0 1];
    box.Pose = transformation;
    walls{13} = box;
    
    left_wall_s7 =  struct("x", .5, "y", 4.2, "z", 0.9, "origin", [6.35+1.6; 0; 1.25]);
    box = collisionBox(left_wall_s7.x, left_wall_s7.y, left_wall_s7.z);
    transformation = [eye(3) left_wall_s7.origin; 0 0 0 1];
    box.Pose = transformation;
    walls{14} = box;

    right_wall = {
        struct("x", .5, "y", 4.2, "z", 1.7, "origin", [.25+1.6; 0; -3.95]),
        struct("x", .5, "y", 1.3, "z", 1.6, "origin", [.25+1.6; 1.45; -2.3]),
        %bottom left straight strip
        struct("x", .5, "y", 1.3, "z", 1.6, "origin", [.25+1.6; -1.45; -2.3]), 
        %struct("x", .5, "y", 4.2, "z", 0.7, "origin", [.25+1.6; 0; -1.15]),
        struct("x", .5, "y", 1.3, "z", 1.6, "origin", [.25+1.6; 1.45; 0]),
        struct("x", .5, "y", 1.3, "z", 1.6, "origin", [.25+1.6; -1.45; 0]),
        struct("x", .5, "y", 4.2, "z", 0.9, "origin", [.25+1.6; 0; 1.25]),
   };
    left_wall = {
        struct("x", .5, "y", 4.2, "z", 1.7, "origin", [6.35+1.6; 0; -3.9]),
        struct("x", .5, "y", 1.3, "z", 1.6, "origin", [6.35+1.6; 1.45; -2.3]),
        struct("x", .5, "y", 1.3, "z", 1.6, "origin", [6.35+1.6; -1.45; -2.3]),
        %struct("x", .5, "y", 4.2, "z", 0.7, "origin", [6.35+1.6; 0; -1.15]),
        struct("x", .5, "y", 1.3, "z", 1.6, "origin", [6.35+1.6; 1.45; 0]),
        struct("x", .5, "y", 1.3, "z", 1.6, "origin", [6.35+1.6; -1.45; 0]),
        struct("x", .5, "y", 4.2, "z", 0.9, "origin", [6.35+1.6; 0; 1.25]),
    };
    boxes = [right_wall;left_wall];

    walls = {};
    
    for i=1:length(boxes)
        wall = boxes{i};
        box = collisionBox(wall.x, wall.y, wall.z);
        transformation = [eye(3) wall.origin; 0 0 0 1];
        box.Pose = transformation;
        walls{end+1} = box;
    end
end