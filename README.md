# Color-detection-using-opencv
## Chapter 1
# Introduction 

Pixels in an image that match a certain color or range of colors are identified by a color detection algorithm. The identified pixels can then be distinguished from the rest of the image by changing their color.
The RGB color model is an additive color scheme that uses different combinations of the red, green, and blue fundamental wavelengths of light to create a wide range of colors. Red, Green, and Blue are the three basic primary colors that make up the model's name.
 
Color information is required for both the classification of color photos and the real-time color sensor, which influence the classification of video images and the precise measurement of real-time temperature. This study suggests a ground-breaking real-time color image classification method based on color similarity in the RGB color space. A color-class map is produced by first identifying the dominant color using the RGB color and luminance information, followed by an estimation of color similarity using the specified calculation method of color component. Using information from the related color-class map, the pixels are then categorized. Due to the fact that infrared paints have color values that change in real time as the temperature changes, the classification results of thermal ink can be used as a real-time color sensor. Then, we also propose a method of color correction and light source compensation to compensate for any possible measurement error. We discuss the proposed classification method application combining with color sensor (thermal ink) in real-time color image classification for Networked Embedded System by the application in fire detection and give a quick overview of a new technique in identifying fire in a video based on these characteristics.

 

The process of finding the name of any color is called color detection. For individuals, this project is actually quite straightforward, but for computers, it is more difficult. The eyes and brains of living organisms transform light into color. Light receptors in our eyes communicate with the brain. Our brain then recognises the color. Since we were young children, we have connected particular lights with their corresponding colors. We'll take a similar process to find names for the colors. I have prepared the project using python. With the help of this Python color detection project, you will be able to click on any color to find out its name right away. Therefore, a data file containing the color's name and values will exist for this. The separation between each color will next be measured to determine which has the smallest distance.










## Chapter 2
# Literature Survey
## Color detection using machine learning.
This was the source of information or body of material that was consulted in order to learn and advance.
With computer vision, colors and their diversity have been revealed over time. Rubin noted that while color is one of the most fascinating and essential aspects of vision, the majority of colorimetry models and techniques have been created outside of the field of optometry. His work provides a brief history of the developments that lead to our current understanding of the complex phenomena of color, as well as an overview of some of the most well-known color models. A simple program made by Behic assisted in identifying the colors in an image. The RGB values of the colors were also returned by the application, which was quite useful. The knowledge of RGB values by many graphic and web designers might be useful. They say a good project to start with in computer vision is building a color recognizer. A study that describes the concepts and methods of color science was proposed by Wyszecki and Stiles. Here, the image's shading is recognized using the RGB display. The RGB display is a color scheme that combines red, green, and blue lights in different ways to produce a range of colors. Berns and Reiman highlighted in their study how image categorization separates a picture into its various parts or components. The degree of categorization relies on the problem that needs to be solved. One of the most challenging issues in the field of image processing is non-trivial picture classification. The success or failure of a computer-based analysis tool is ultimately determined by how accurately the classification was made. Gonzalez explains in his study that MATLAB treats each response as a network, making it the most often used picture preparation stage for images that speak to grey scale, RGB, HSV, and other shading models. Additionally, methods for detecting the shapes and colors of previously introduced objects are discussed using MATLAB. Abadpour and Kasaei also instruct readers on how to convert RGB images to grayscale images, then to binary images, among other things, however the topic of form recognition doesn't appear to be covered. The color image processing described in the study utilizing principal element analysis includes a comparison of each pixel inside the metric, which determines the dominant color because the color of the provided object is described. Senthamaraikannan, Shriram, and William suggest novel real-time color recognition capabilities in their article real-time color recognition, i.e., extracting fundamental colors for the purpose of vision-based human-computer interaction. By addressing these issues, vision-based human-computer interaction can be accomplished by evaluating segmental primary color regions with a primary focus on color-based image classification and vision-based color identification. This challenge is made challenging by crowded backgrounds, unknowable lighting conditions, and numerous moving objects. In light of everything that had happened, Bhanot continued to guide the stroll in an entirely different route. This author had a keen interest in images in Python. The author began to explore if information could be extracted from such photographs using machine learning after discovering OpenCV, which enables the import and manipulation of images in Python. Online searching has been observed to be possible based on a number of filters, one of which being color. It was this inspiration that led the author to actually create the code needed to extract colors from photographs and filter them using those extracted colors.  Additionally, Ray and Rose demonstrate in their paper how to understand the fundamentals of OpenCV, how to extract colors from photos using the KMeans algorithm, and how to filter images from a collection of photographs based on RGB color values. This opens the door for a wide range of innovative uses, such as looking for specific colors in apparel or in a search engine. Many buyers are interested in the topic of color detection. There are several ways to identify colors, from traditional physical techniques to cutting-edge machine learning and even web scraping techniques. We have the major color spaces at our disposal to help with color detection thanks to some of the popular techniques that have been listed below. One of these has already been mentioned.


## Chapter 3
# Methodology
There are two types of color sensors. One recognizes the three various color types in the receiver and casts a wide-spectrum light on the object. The alternate technique separately shines three different light colors on the thing (red, blue, and green).
Red, blue, and green light intensities are measured and the received light ratio is calculated in both situations.
The primary colors that make up all other hues are red, green, and blue. A computer's defined color values fall between 0 and 255. How many distinct ways can a color be described? 16,581,375, or 256*256*256, is the answer. There are around 16.5 million possible ways to depict a color.



???	Colors.csv

 




The RGB color space, which is used to produce other colors, is made up of the three primary hues red, green, and blue. The RGB representation is shown in the figure using the Cartesian coordinate system. The three axes correspond to R, G, and B, and each point in the three-dimensional space represents one of the three brightness value components. The brightness value is between one and zero.
The farthest vertex from the origin of the figure is white, with a value of (0,0,0), while the origin is black, with a value of (0,0,0). (1,1,1). The transition of the grey value from black to white is referred to as the "grey line," which is a straight line between them. The final three corners???yellow, cyan, and magenta???represent the complementary color of the three fundamental colors.
 



For this project, we'll need three main modules. They are OpenCV, Pandas, and NumPy. OpenCV is a real-time application-focused library that is highly efficient. A free and open-source software library for computer vision and machine learning is called OpenCV. In order to speed up the incorporation of artificial intelligence into commercial goods, OpenCV was created to offer a standard infrastructure for computer vision applications.
To modify data sets, utilize the Pandas library in Python. It provides resources for exploring, organizing, analyzing, and manipulating data. The name "Pandas," which stands for both "Panel Data" and "Python Data Analysis," was created by Wes McKinney in 2008.

