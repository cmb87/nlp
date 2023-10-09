text_data_arr = [
    '''An airfoil (American English) or aerofoil (British English) is a streamlined body that is capable of generating significantly more lift than drag. Wings, sails and propeller blades are examples of airfoils. Foils of similar function designed with water as the working fluid are called hydrofoils.
When oriented at a suitable angle, a solid body moving through a fluid deflects the oncoming fluid (for fixed-wing aircraft, a downward force), resulting in a force on the airfoil in the direction opposite to the deflection. This force is known as aerodynamic force and can be resolved into two components: lift (perpendicular to the remote freestream velocity) and drag (parallel to the freestream velocity).
The lift on an airfoil is primarily the result of its angle of attack. Most foil shapes require a positive angle of attack to generate lift, but cambered airfoils can generate lift at zero angle of attack. Airfoils can be designed for use at different speeds by modifying their geometry: those for subsonic flight generally have a rounded leading edge, while those designed for supersonic flight tend to be slimmer with a sharp leading edge. All have a sharp trailing edge.
The air deflected by a aerofoil causes the airfoil to generate behind a lower-pressure "shadow" above and behind itself. This pressure difference is accompanied by a velocity difference, via Bernoulli's principle, so the resulting flowfield about the airfoil has a higher average velocity on the upper surface than on the lower surface. In some situations (e.g. inviscid potential flow) the lift force can be related directly to the average top/bottom velocity difference 
without computing the pressure by using the concept of circulation and the Kutta–Joukowski theorem.
''',
'''The wings and stabilizers of fixed-wing aircraft, as well as helicopter rotor blades, are built with airfoil-shaped cross sections. 
Airfoils are also found in propellers, fans, compressors and turbines. Sails are also airfoils, and the underwater surfaces of sailboats,
 such as the centerboard, rudder, and keel, are similar in cross-section and operate on the same principles as airfoils. Swimming 
 and flying creatures and even many plants and sessile organisms employ airfoils/hydrofoils: common examples being bird wings, the
  bodies of fish, and the shape of sand dollars. An airfoil-shaped wing can create downforce on an automobile or other motor vehicle, improving traction.
When the wind is obstructed by an object such as a flat plate, a building, or the deck of a bridge, the object will experience drag 
and also an aerodynamic force perpendicular to the wind. This does not mean the object qualifies as an airfoil. 
Airfoils are highly-efficient lifting shapes, able to generate more lift than similarly sized flat plates of the same area, 
and able to generate lift with significantly less drag. Airfoils are used in the design of aircraft, propellers, rotor blades, 
wind turbines and other applications of aeronautical engineering.
A lift and drag curve obtained in wind tunnel testing is shown on the right. The curve represents an airfoil with a positive 
camber so some lift is produced at zero angle of attack. With increased angle of attack, lift increases in a roughly linear 
relation, called the slope of the lift curve. At about 18 degrees this airfoil stalls, and lift falls off quickly beyond that. 
The drop in lift can be explained by the action of the upper-surface boundary layer, which separates and greatly thickens over 
the upper surface at and past the stall angle. The thickened boundary layer's displacement thickness changes the airfoil's effective shape, 
in particular it reduces its effective camber, which modifies the overall flow field so as to reduce the circulation and the lift.
The thicker boundary layer also causes a large increase in pressure drag, so that the overall drag increases sharply near and past
the stall point.Airfoil design is a major facet of aerodynamics. Various airfoils serve different flight regimes. Asymmetric airfoils
 can generate lift at zero angle of attack, while a symmetric airfoil may better suit frequent inverted flight as in an aerobatic airplane. 
 In the region of the ailerons and near a wingtip a symmetric airfoil can be used to increase the range of angles of attack to avoid spin–stall. 
 Thus a large range of angles can be used without boundary layer separation. Subsonic airfoils have a round leading edge, which is naturally
insensitive to the angle of attack. The cross section is not strictly circular, however: the radius of curvature is increased before the wing
achieves maximum thickness to minimize the chance of boundary layer separation. This elongates the wing and moves the point of maximum thickness
 back from the leading edge. Supersonic airfoils are much more angular in shape and can have a very sharp leading edge, which is very sensitive 
 to angle of attack. A supercritical airfoil has its maximum thickness close to the leading edge to have a lot of length to slowly shock the supersonic
  flow back to subsonic speeds. Generally such transonic airfoils and also the supersonic airfoils have a low camber to reduce drag divergence.
   Modern aircraft wings may have different airfoil sections along the wing span, each one optimized for the conditions in each section of the wing.
Movable high-lift devices, flaps and sometimes slats, are fitted to airfoils on almost every aircraft. A trailing edge flap acts similarly to an 
aileron; however, it, as opposed to an aileron, can be retracted partially into the wing if not used.
A laminar flow wing has a maximum thickness in the middle camber line. Analyzing the Navier–Stokes equations in the linear regime shows that
 a negative pressure gradient along the flow has the same effect as reducing the speed. So with the maximum camber in the middle, maintaining
  a laminar flow over a larger percentage of the wing at a higher cruising speed is possible. However, some surface contamination will disrupt
   the laminar flow, making it turbulent. For example, with rain on the wing, the flow will be turbulent. Under certain conditions, insect 
   debris on the wing will cause the loss of small regions of laminar flow as well. Before NASA's research in the 1970s and 1980s the aircraft 
   design community understood from application attempts in the WW II era that laminar flow wing designs were not practical using common
    manufacturing tolerances and surface imperfections. That belief changed after new manufacturing methods were developed with composite 
    materials (e.g. laminar-flow airfoils developed by Professor Franz Wortmann for use with wings made of fibre-reinforced plastic). 
    Machined metal methods were also introduced. NASA's research in the 1980s revealed the practicality and usefulness of laminar flow
     wing designs and opened the way for laminar-flow applications on modern practical aircraft surfaces, 
from subsonic general aviation aircraft to transonic large transport aircraft, to supersonic designs. Schemes have been devised to define
 airfoils – an example is the NACA system. Various airfoil generation systems are also used. An example of a general purpose airfoil that finds
  wide application, and pre–dates the NACA system, is the Clark-Y.
Today, airfoils can be designed for specific functions by the use of computer programs.''',
'''The various terms related to airfoils are defined below:

The suction surface (a.k.a. upper surface) is generally associated with higher velocity and lower static pressure.
The pressure surface (a.k.a. lower surface) has a comparatively higher static pressure than the suction surface. The pressure gradient between these two surfaces contributes to the lift force generated for a given airfoil.
The geometry of the airfoil is described with a variety of terms :

The leading edge is the point at the front of the airfoil that has maximum curvature (minimum radius).
The trailing edge is defined similarly as the point of maximum curvature at the rear of the airfoil.
The chord line is the straight line connecting leading and trailing edges. The chord length, or simply chord, c, is the length of the chord line. That is the reference dimension of the airfoil section.
''',
'''
The shape of the airfoil is defined using the following geometrical parameters:
The mean camber line or mean line is the locus of points midway between the upper and lower surfaces. Its shape depends on the thickness distribution along the chord;
The thickness of an airfoil varies along the chord. It may be measured in either of two ways:
Thickness measured perpendicular to the camber line. This is sometimes described as the "American convention";
Thickness measured perpendicular to the chord line. This is sometimes described as the "British convention".
Some important parameters to describe an airfoil's shape are its camber and its thickness. For example, an airfoil of the NACA 4-digit series 
such as the NACA 2415 (to be read as 2 – 4 – 15) describes an airfoil with a camber of 0.02 chord located at 0.40 chord, with 0.15 chord of maximum thickness.
Finally, important concepts used to describe the airfoil's behaviour when moving through a fluid are:
The aerodynamic center, which is the chord-wise location about which the pitching moment is independent of the lift coefficient and the angle of attack.
The center of pressure, which is the chord-wise location about which the pitching moment is momentarily zero. 
On a cambered airfoil, the center of pressure is not a fixed location as it moves in response to changes in angle of attack and lift coefficient.
''',
'''
Thin airfoil theory is a simple theory of airfoils that relates angle of attack to lift for incompressible, inviscid flows. It was devised by German mathematician Max Munk and further refined by British aerodynamicist Hermann Glauert and others in the 1920s. The theory idealizes the flow around an airfoil as two-dimensional flow around a thin airfoil. It can be imagined as addressing an airfoil of zero thickness and infinite wingspan.
Thin airfoil theory was particularly notable in its day because it provided a sound theoretical basis for the following important properties of airfoils in two-dimensional inviscid flow:
on a symmetric airfoil, the center of pressure and aerodynamic center are coincident and lie exactly one quarter of the chord behind the leading edge.
on a cambered airfoil, the aerodynamic center lies exactly one quarter of the chord behind the leading edge, but the position of the center of pressure moves when the angle of attack changes.
Thin airfoil theory does not account for the stall of the airfoil, which usually occurs at an angle of attack between 10° and 15° for typical airfoils.
In the mid-late 2000s, however, a theory predicting the onset of leading-edge stall was proposed by Wallace J. Morris II in his doctoral thesis.
Morris's subsequent refinements contain the details on the current state of theoretical knowledge on the leading-edge stall phenomenon.
Morris's theory predicts the critical angle of attack for leading-edge stall onset as the condition at which a global separation zone is
predicted in the solution for the inner flow. Morris's theory demonstrates that a subsonic flow about a thin airfoil can be described
 in terms of an outer region, around most of the airfoil chord, and an inner region, around the nose, that asymptotically match each other.
  As the flow in the outer region is dominated by classical thin airfoil theory, Morris's equations exhibit many components of thin airfoil theory.
''',
'''
Compressible flow (or gas dynamics) is the branch of fluid mechanics that deals with flows having significant changes in fluid density. 
While all flows are compressible, flows are usually treated as being incompressible when the Mach number (the ratio of the speed of the
 flow to the speed of sound) is smaller than 0.3 (since the density change due to velocity is about 5% in that case). The study of compressible flow is relevant
  to high-speed aircraft, jet engines, rocket motors, high-speed entry into a planetary atmosphere, gas pipelines,
   commercial applications such as abrasive blasting, and many other fields.
''',
'''
The study of gas dynamics is often associated with the flight of modern high-speed aircraft and atmospheric reentry of space-exploration 
vehicles; however, its origins lie with simpler machines. At the beginning of the 19th century, investigation into the behaviour of fired
bullets led to improvement in the accuracy and capabilities of guns and artillery. As the century progressed, inventors such as
Gustaf de Laval advanced the field, while researchers such as Ernst Mach sought to understand the physical phenomena involved through
experimentation. At the beginning of the 20th century, the focus of gas dynamics research shifted to what would eventually become the
 aerospace industry. Ludwig Prandtl and his students proposed important concepts ranging from the boundary layer to supersonic shock 
 waves, supersonic wind tunnels, and supersonic nozzle design. Theodore von Kármán, a student of Prandtl, continued to improve 
 the understanding of supersonic flow. Other notable figures (Meyer, Luigi Crocco, and Ascher Shapiro) also contributed significantly 
 to the principles considered fundamental to the study of modern gas dynamics. Many others also contributed to this field.
  Accompanying the improved conceptual understanding of gas dynamics in the early 20th century was a public misconception 
  that there existed a barrier to the attainable speed of aircraft, commonly referred to as the "sound barrier." In truth, 
  the barrier to supersonic flight was merely a technological one, although it was a stubborn barrier to overcome. 
  Amongst other factors, conventional aerofoils saw a dramatic increase in drag coefficient when the flow approached 
  the speed of sound. Overcoming the larger drag proved difficult with contemporary designs, thus the perception of a sound barrier. 
  However, aircraft design progressed sufficiently to produce the Bell X-1. Piloted by Chuck Yeager, the X-1 officially achieved supersonic speed in October 1947.
Historically, two parallel paths of research have been followed in order to further gas dynamics knowledge.
 Experimental gas dynamics undertakes wind tunnel model experiments and experiments in shock tubes and ballistic 
 ranges with the use of optical techniques to document the findings. Theoretical gas dynamics considers the equations of motion applied t
 o a variable-density gas, and their solutions. Much of basic gas dynamics is analytical, but in the modern era Computational 
 fluid dynamics applies computing power to solve the otherwise-intractable nonlinear partial differential 
 equations of compressible flow for specific geometries and flow characteristics.
'''
]