* [公开的建筑领域的数据集](#公开的建筑领域的数据集)
   * [1 竞赛](#竞赛)
      * [1.1 已结束的竞赛](#已结束的竞赛)
      * [1.2 正在进行的竞赛](#正在进行的竞赛)
   * [2 数据集](#数据集)
      * [2.1 文本数据集](#文本数据集)
      * [2.2 图片数据集](#图片数据集)
         * [2.2.1 建筑平面图](#建筑平面图)
         * [2.2.2 卫星图/航空图/SAR等](#卫星图/航空图/SAR等)
         * [2.2.3 街景照片](#街景照片)
         * [2.2.4 单体建筑照片](#单体建筑照片)
      * [2.3 模型数据集](#模型数据集)
      * [2.4 结构化数据集](#结构化数据集) 
   * [3 相关大模型](#相关大模型)

# 公开的建筑领域的数据集（230818更新）

# 1. 竞赛

## 1. 1 已结束的竞赛

- **SpaceNet 1: Building Detection v1**
    
    项目简介：数据集为里约热内卢建筑物轮廓卫星图。使用了一个称为YOLT的改进版YOLO模型进行基线性能测试。
    
    竞赛组织方：SpaceNet是由IQT Labs的CosmiQ Works和Maxar（当时的DigitalGlobe）在2016年8月创立的。这个非正式的合作旨在加速开源机器学习能力，特别是针对地理空间用例，提供一个免费可用的图像库，其中包含了配准的地图特征。
    
    竞赛时间：2017年；
    
    [项目地址](https://spacenet.ai/spacenet-buildings-dataset-v1/)
    
    [相关论文](https://arxiv.org/pdf/1807.01232.pdf)
    
- **SpaceNet 2: Building Detection v2**
    
    项目简介：拉斯维加斯、巴黎、上海、喀土穆建筑物轮廓卫星图。第二次建筑物挑战的结果远好于第一次。使用YOLT和MNC的改进版进行基线性能测试。
    
    竞赛组织方：SpaceNet是由IQT Labs的CosmiQ Works和Maxar（当时的DigitalGlobe）在2016年8月创立的。这个非正式的合作旨在加速开源机器学习能力，特别是针对地理空间用例，提供一个免费可用的图像库，其中包含了配准的地图特征。
    
    竞赛时间：2017年；
    
    [项目地址](https://spacenet.ai/spacenet-buildings-dataset-v2/)
    
    [相关论文](https://arxiv.org/pdf/1807.01232.pdf)
    
- **2018 Open AI Tanzania Building Footprint Segmentation Challenge**
    
    项目简介：Open AI Tanzania 邀请数据科学家开发特征检测算法，这些算法可以自动识别坦桑尼亚无人机驾驶员通过桑给巴尔地图倡议（ZMI）收集的高分辨率航空图像中的建筑物和建筑类型。这个挑战的目标是正确地切割并分类处于各种建设阶段的建筑物占地面积。
    
    竞赛组织方：Open AI Tanzania
    
    竞赛时间：2018年
    
    [项目地址](https://competitions.codalab.org/competitions/20100)
    
- **DEEPGLOBE：CVPR 2018 - Satellite Challenge**
    
    项目简介：这个竞赛围绕三个不同的卫星图像理解任务进行结构化。为此比赛创建和发布的数据集可能作为未来卫星图像分析研究的参考基准。此外，由于挑战任务将涉及经典计算机视觉问题的"野生"形式，这些数据集有可能成为设计强大视觉算法的宝贵测试平台，超越了遥感领域。
    
    竞赛组织方：facebook, MIT, 普渡大学，达特茅斯背景的研究人员发起
    
    竞赛时间：2018年
    
    [项目地址](http://deepglobe.org/index.html)
    
- **SpaceNet 4: Off-Nadir Buildings**
    
    项目简介：这个挑战的主要目标是从越来越偏离轴线的卫星图像中提取建筑物的轮廓。
    
    竞赛组织方：SpaceNet是由IQT Labs的CosmiQ Works和Maxar（当时的DigitalGlobe）在2016年8月创立的。这个非正式的合作旨在加速开源机器学习能力，特别是针对地理空间用例，提供一个免费可用的图像库，其中包含了配准的地图特征。
    
    竞赛时间：2019年；
    
    [项目地址](https://spacenet.ai/off-nadir-building-detection/)
    
    [相关论文](https://arxiv.org/abs/1903.12239)
    
- ****2020数字中国创新大赛—应用赛1：建筑智能普查****
    
    项目简介：本赛事由福建省有关部门挑选出16个具有代表性的实验区，对于每个实验区，选取没有云雾遮挡的中国高分二号卫星遥感影像。初赛阶段，参赛队伍使用高分二号遥感影像及其标记数据训练模型，并对训练集影像进行建筑物提取。复赛阶段，选手将提交自己的模型测试docker镜像来由天池统一测试；
    
    竞赛组织方：数字中国建设峰会组委会；
    
    竞赛时间：2020年
    
    [项目地址](https://tianchi.aliyun.com/competition/entrance/231767/information)
    
- ****IEEE-CIS 3rd Technical Challenge****
    
    项目简介：IEEE计算智能学会在2021年7月至11月期间举办了一场基于可再生能源数据的预测和优化竞赛。数据来自澳大利亚墨尔本维多利亚州莫纳什大学克莱顿校区的六栋建筑和六个太阳能设施。数据的分辨率为15分钟，年份为2016年至2020年。参赛者需要预测2020年10月和11月的太阳能发电量和建筑电力使用量；
    
    竞赛组织方：IEEE Computational Intelligence Society (IEEE-CIS) 和澳大利亚的莫纳什大学共同发起了这个竞赛；
    
    竞赛时间：2021年；
    
    [项目地址](https://ieee-dataport.org/competitions/ieee-cis-technical-challenge-predictoptimize-renewable-energy-scheduling)
    
- ****Computer Vision in the Built Environment****
    
    项目简介：为了进一步建立这两个领域之间的联系，迈向理想的建筑流程，研讨会通过举办Scan-to-BIM挑战赛，重点探索如何将激光雷达、摄影测量或深度地图相机获得的三维点云数据转换为建筑信息模型(BIM)和平面图(FloorPlan);
    
    竞赛组织方：建成环境计算机视觉研讨会是由苏黎世联邦理工学院主办，旨在将建筑、工程和建筑(AEC)领域与计算机视觉领域联系起来，解决与AEC社区相关的问题，比如了解建筑工地的变化，以及从真实数据扫描中自动生成建筑模型等现实世界问题。如果这些问题得到解决，将对这个数万亿美元的行业以及全球的整体生活质量产生切实的影响;
    
    竞赛时间：2023年第3届;
    
    [项目地址](https://cv4aec.github.io/)
  

## 1. 2 正在进行的竞赛：

## 2 数据集

### 2.1 文本数据集

- **Houses-dataset**
    - 项目简介：这是一个包含视觉和文本信息的房价基准数据集。每个房屋都由卧室、浴室、厨房和房屋正面的四张图片来表示。这是第一个包含用于估算房价的图片的数据集；
    - 数据类型：结合了图像和文本的房屋数据集；
    - 数据量级：由美国加利福尼亚州的535个样本房屋组成；数据集包含2140张图片，每个房屋有4张图片；还有一个包含数据集文本元数据的文本文件；
    - 发布机构及时间：由开罗美国大学于2016年发布；
    - [项目地址](https://github.com/emanhamed/Houses-dataset)
    - [相关论文](https://arxiv.org/pdf/1609.08399.pdf)
- **Intelligent Home 3D**
    - 项目简介：第一个文本到3D房屋模型的数据集；
    - 数据类型：图像和文本；
    - 数据量级：包含2000栋房屋，13478个房间和873个纹理图像以及相应的自然语言描述。建筑布局生成中使用1600对数据进行训练，400对数据进行测试；纹理合成中，使用503个数据进行训练，370个数据进行测试；
    - 发布机构及时间：由华南理工大学，广州实验室，澳大利亚阿德莱德大学机器视觉中心，酷家乐公司于2020年发布；
    - [项目地址](https://github.com/chenqi008/HPGM)
    - [相关论文](https://arxiv.org/pdf/2003.00397v1.pdf)
- ****ART（AutoRuleTransform）****
    - 项目简介：介绍了一种集成自然语言处理（NLP）和上下文无关语法（CFG）的自动规则解释方法，为了实现建筑规范的自动化的合规性检查，使用的数据集
    - 数据类型：规范文本；
    - 数据量级：收集了30,000条规范（经过句子分割后）；识别出其中的3,660条规范具有定量要求；随机选择了1,000条规范作为候选，最终得到了611条规范组成的数据集；
    - 发布机构及时间：由清华大学水土学院于2022年发布；
    - [项目地址](https://github.com/smartaec/auto-rule-transform)
    - [相关论文](https://www.sciencedirect.com/science/article/abs/pii/S0166361522001439?via%3Dihub)，[相关论文2](https://www.sciencedirect.com/science/article/abs/pii/S0926580522003971?via%3Dihub)

### 2.2 图片数据集

#### 2.2.1 建筑平面图

- **Houses-dataset**
    - 项目简介：一个大规模的CAD绘图数据集。为了克服知识产权的限制，从每个大型平面图中只裁剪了一小部分，并移除了可能传达机密信息的敏感文本。最后，数据集中的平面图块只包含几何和结构信息；
    - 数据类型：CAD矢量平面图；
    - 数据量级：超过10,000个楼层平面图，范围从住宅到商业建筑；
    - 发布机构及时间：由阿里巴巴人工智能实验室和加拿大西蒙弗雷泽大学于2021年发布；
    - [项目地址](https://floorplancad.github.io/)
    - [相关论文](https://openaccess.thecvf.com/content/ICCV2021/papers/Fan_FloorPlanCAD_A_Large-Scale_CAD_Drawing_Dataset_for_Panoptic_Symbol_Spotting_ICCV_2021_paper.pdf)
- ****Path Finding Simulation Dataset (PFSD)****
    - 项目简介：寻路模拟数据集（Path Finding Simulation Dataset）是通过在100个大型合成环境中模拟代理（agents）导航来生成的。这些环境是根据当代建筑中常见的房间和走廊的外部形状和内部组织设计的。代理通过使用障碍物之间的出口从一个房间移动到另一个房间来寻找路径。
    - 数据类型：主要包括各种环境和移动行为的轨迹。这些轨迹信息被表示为高斯热力图，其中每个未来的步骤都被表示为每步一个热力图。热力图的大小与语义地图的大小相匹配；
    - 数据量级：每个环境都被用来模拟500个场景（总共50,000个场景），在这些场景中，单个代理使用普遍的社会力模型在环境内的两个随机点之间导航。使用PFSD的子集，并分别使用40/2/4个不同的合成环境制作训练/验证/测试集。
    - 发布机构及时间：由Rutgers University，The College of New Jersey于2022年发布；
    - [项目地址](https://ml1323.github.io/MUSE-VAE/dataset/)
    - [相关论文](https://openaccess.thecvf.com/content/CVPR2022/papers/Lee_MUSE-VAE_Multi-Scale_VAE_for_Environment-Aware_Long_Term_Trajectory_Prediction_CVPR_2022_paper.pdf)

#### 2.2.2 卫星图/航空图/SAR等

- ****SZTAKI AirChange Benchmark set****
    - 项目简介：项目主要研究了在航空照片中进行变化检测的混合马尔可夫模型，特别是在有大时间差异的情况下。作者提出了一个新的混合马尔可夫模型，通过在真实世界的航空图像上进行验证，证明了该方法的有效性；
    - 数据类型：航空图像；
    - 数据量级：包含13对航空图像，每对图像的尺寸为952x640，分辨率为1.5m/像素；
    - 发布机构及时间：由匈牙利科学院的计算机科学与控制研究所以及Google Earth匈在2008年发布；
    - [项目地址](http://web.eee.sztaki.hu/remotesensing/airchange_benchmark.html)
    - [相关论文](https://www.researchgate.net/publication/220052302_Change_Detection_in_Optical_Aerial_Images_by_a_Multilayer_Conditional_Mixed_Markov_Model)，[相关论文2](https://www.researchgate.net/publication/224375388_A_Mixed_Markov_Model_for_Change_Detection_in_Aerial_Photos_with_Large_Time_Differences)
- **Massachusetts Buildings Dataset**
    - 项目简介：是一个大规模的建筑物检测数据集，主要包含了美国波士顿地区的航拍图像和对应的建筑物标签；
    - 数据类型：航拍图片；
    - 数据量级：共151张，被随机分为137张训练图像，10张测试图像和4张验证图像；
    - 发布机构及时间：由多伦多大学于2013年发布；
    - [项目地址](https://www.cs.toronto.edu/~vmnih/data/)
    - [相关论文](https://www.cs.toronto.edu/~vmnih/docs/Mnih_Volodymyr_PhD_Thesis.pdf)
- **Inria Aerial Image Labeling dataset**
    - 项目简介：一个航空图像标记数据集，该数据集覆盖了各种城市环境的外观，包括不同的地理位置；
    - 数据类型：航空图像；
    - 数据量级：训练集包括Austin, TX; Chicago, IL; Kitsap County, WA; Vienna, Austria; West Tyrol, Austria，每个地区36个图块，总面积405平方公里；测试集包括Bellingham, WA; San Francisco, CA; Bloomington, IN; Innsbruck, Austria; East Tyrol, Austria，每个地区36个图块，总面积405平方公里。
    - 发布机构及时间：由法国国家信息与自动化研究所于2017年发布；
    - [项目地址](https://project.inria.fr/aerialimagelabeling/)
    - [相关论文](https://inria.hal.science/hal-01468452/document)
- **ABCD (AIST Building Change Detection)**
    - 项目简介：一个标注数据集，专门用于构建和评估损害检测系统，以确定建筑物是否被海啸冲走；
    - 数据类型：成对的海啸前后的航空影像块，并且在块的中心包含一个目标建筑物。这些对子是从日本东北地区的大量RGB航空影像中裁剪出来的。这些航空影像在大东日本地震前后拍摄，原始像素分辨率为地震前的影像为40厘米，地震后的影像为12厘米（实际上，重新采样到40厘米）；
    - 数据量级：包括8506对固定比例的对子和8444对调整大小的对子；
    - 发布机构及时间：由日本的高级工业科学技术研究所（Advanced Industrial Science and Technology）和名古屋大学（Nagoya University）于2017年发布；
    - [项目地址](https://github.com/gistairc/ABCDdataset)
    - [相关论文](https://www.mva-org.jp/Proceedings/2017USB/papers/01-02.pdf)
- **WHU Building Dataset**
    - 项目简介：武汉大学创建的一个建筑数据集，称为WHU建筑数据集。这个数据集包含了从航空和卫星图像中手动提取的建筑样本。含有4个数据集：航空图像数据集，卫星图像数据集I（全球城市），卫星图像数据集II（东亚）和建筑变化检测数据集。
    - 数据类型：航空图像和卫星图像；
    - 数据量级：**航空图像数据集中**包含了从新西兰基督城的航空图像中提取的超过220,000个独立建筑，图像被分割成了8,189个512×512像素的片，其中包含了训练集（130,500个建筑），验证集（14,500个建筑）和测试集（42,000个建筑）。**卫星图像数据集I（全球城市）中**收集了来自全球各城市的图像，包含了204个图像。**卫星图像数据集II（东亚）中**包含了34085个建筑。**建筑变化检测数据集中**覆盖了2011年2月发生6.3级地震并在随后几年重建的区域，这个数据集包含了2012年4月获取的航空图像，其中包含了20.5平方公里的区域内的12796个建筑（在2016年的数据集中，同一区域有16077个建筑）；
    - 发布机构及时间：由武汉大学于2018年发布；
    - [项目地址](http://gpcv.whu.edu.cn/data/building_dataset.html)
    - [相关论文](https://ieeexplore.ieee.org/document/8444434)
- **xBD Dataset**
    - 项目简介：一个新的大规模数据集，用于推动变化检测和建筑物损坏评估的人道援助和灾后恢复研究。在与多个灾害响应机构的合作下，xBD提供了各种灾害事件的前后卫星图像，包括建筑物的多边形、损坏等级的序数标签以及相应的卫星元数据。此外，数据集还包含了环境因素（如火、水、烟等）的边界框和标签；
    - 数据类型：主要是卫星图像，包括建筑物的损坏等级、位置以及其他环境因素的信息；
    - 数据量级：xBD是迄今为止最大的建筑物损坏评估数据集，包含了850,736个建筑物的注释，覆盖了45,362平方公里的图像。
    - 发布机构及时间：由卡内基梅隆大学，软件工程研究所，国防创新单位，国防部和CrowdAI, Inc.于2019年发布；
    - [项目地址](https://xview2.org/dataset)
    - [相关论文](https://arxiv.org/pdf/1911.09296.pdf)
- **Rwanda Built-up Region Segmentation Dataset**
    - 项目简介：创建了一个真实且具有挑战性的高分辨率数据集，通过手动标记卢旺达的73.4平方公里，捕获了不同地形上的各种建筑结构。主要目标是提出一种新的领域适应算法，以处理卫星和航空图像带来的挑战，并在建筑区域分割问题上展示其有效性。
    - 数据类型：卫星和航空图像；
    - 数据量级：手动标记的卢旺达的73.4平方公里创建的，收集了总共787张高分辨率（每像素1.193米）的卫星图像，每张图像的大小为256×256。这些图像捕获了不同地形上的各种建筑结构，包括森林和沙漠中的建筑区域、泥房子、锡和彩色屋顶等；
    - 发布机构及时间：由巴基斯坦的信息技术大学于2020年发布；
    - [项目地址](http://im.itu.edu.pk/wan/)
    - [相关论文](https://www.sciencedirect.com/science/article/abs/pii/S0924271620301829)
- **Synthinel-1**
    - 项目简介：该数据集由具有像素级建筑标签的多样化虚拟环境组成。将Synthinel-1用作实际训练图像的增强可以提高CNN的性能，尤其是在新的地理位置或条件下；
    - 数据类型：为合成的航空图像数据集；
    - 数据量级：
    - 发布机构及时间：由杜克大学于2020年发布；
    - [项目地址](https://github.com/timqqt/Synthinel)
    - [相关论文](https://arxiv.org/abs/2001.05130)
- **LEVIR-CD**
    - 项目简介：LEVIR-CD是一个新的大规模遥感建筑变化检测数据集；
    - 数据类型：遥感图像。具体来说，这些图像是由Google Earth Engine收集的，包括了城市地区的建筑物变化；
    - 数据量级：包含了637个大区域，总共有22690对双时相图像；
    - 发布机构及时间：由中国科学院的学习、视觉和遥感实验室于2020年发布；
    - [项目地址](http://chenhao.in/LEVIR/)
    - [相关论文](https://www.mdpi.com/2072-4292/12/10/1662)
- **The S2Looking dataset**
    - 项目简介：这是一个专门用于建筑变化检测的卫星侧视图像数据集。该数据集包含了5000对农村地区的双时相图像；
    - 数据类型：RGB图像，图像的分辨率为0.5∼0.8米，图像的大小为1024 × 1024像素；
    - 数据量级：总图像对数为5000对；
    - 发布机构及时间：由浙江大学和浙江工业大学于2021年发布；
    - [项目地址](https://github.com/S2Looking/Dataset)
    - [相关论文](https://arxiv.org/pdf/2107.09244v3.pdf)
- **Roof-Image Dataset**
    - 项目简介：是一个屋顶航拍图的数据集；
    - 数据类型：屋顶卫星图像；
    - 数据量级：包含2539个屋顶网格，每个网格都与一张图像配对；
    - 发布机构及时间：阿卜杜拉国王科技大学，阿里巴巴集团和巴黎综合理工学院于2021年发布；
    - [项目地址](https://github.com/llorz/SGA21_roofOptimization/tree/main/RoofGraphDataset)
    - [相关论文](https://arxiv.org/pdf/2109.07683v1.pdf)
- **BONAI（Buildings in Off-Nadir Aerial Images）**
    - 项目简介：这篇论文的数据集类型是航空图像，每个建筑物实例都有完全注释的实例级屋顶、轮廓和相应的偏移向量；
    - 数据类型：航空图像；
    - 数据量级：包含3300张图像，共有268958个建筑物实例；其中，训练集包含上海、北京、成都和哈尔滨四个城市的2680张图像，共有225455个建筑物实例；验证集包含上海和济南两个城市的300张图像，共有22894个建筑物实例；测试集含上海和西安两个城市的300张图像，共有20609个建筑物实例；
    - 发布机构及时间：由武汉大学于2022年发布；
    - [项目地址](https://github.com/jwwangchn/BONAI)
    - [相关论文](https://arxiv.org/abs/2204.13637)
- **SARBuD (SAR Building Dataset)**
    - 项目简介：该数据集是面向深度学习的GF-3精细模式SAR建筑数据集。论文详细介绍了数据集的预处理和样本切片制作过程，包括原始SAR图像的预处理，图像像素级标签的制作，以及样本切片的制作等。此外，论文还对SAR图像进行了增强处理，以提高近海区域的SAR图像建筑区与其他地物的对比度；
    - 数据类型：合成孔径雷达(SAR)图像；
    - 数据量级：大约25000个建筑区域的SAR图像patches和相应的25000个标记的二进制图像；
    - 发布机构及时间：由中国科学院空天信息创新研究院，中国科学院数字地球重点实验室, 中国科学院大学和中国资源卫星应用中心于2022年发布；
    - [项目地址](https://github.com/CAESAR-Radi/SARBuD)
    - [相关论文](https://www.sciencedirect.com/science/article/abs/pii/S0034425721002352)，[相关论文2](http://www.jors.cn/jrs/ch/reader/create_pdf.aspx?file_no=202204003&flag=1)
- **OpenSARUrban**
    - 项目简介：OpenSARUrban是一个用于城市解释的Sentinel-1 SAR图像数据集，包括了多个城市的多种类型的地物，如住宅、商业区、交通枢纽等；
    - 数据类型：合成孔径雷达(SAR)图像；
    - 数据量级：提供了33358个城市场景的SAR图像块，覆盖了中国的21个主要城市；
    - 发布机构及时间：由上海交通大学发布于2022年；
    - [项目地址](https://opensar.sjtu.edu.cn/index.html)
    - [相关论文](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8952866)

#### 2.2.3 街景照片

- ****Google Street View Data Set****
    - 项目简介：Google街景数据集的图片覆盖了宾夕法尼亚州匹兹堡、佛罗里达州奥兰多的市中心及其周边地区，以及部分纽约曼哈顿地区。提供了这些图片的精确GPS坐标和它们的指南针方向；
    - 数据类型：Google街景图片；
    - 数据量级：62,058张；
    - 发布机构及时间：由Center for Research in Computer Vision at the University of Central Florida发布于2014年；
    - [项目地址](https://www.crcv.ucf.edu/papers/PAMI_Amir%20Zamir.pdf)
    - [相关论文](https://www.crcv.ucf.edu/papers/PAMI_Amir%20Zamir.pdf)
- **24/7 Tokyo dataset**
    - 项目简介："24/7 Tokyo"数据集主要包含了在不同时间（包括白天、黄昏和夜晚）拍摄的查询图片。这些图片分布在125个不同的地点，每个地点都有3个不同的观察方向。数据集中的每张图片都是由Apple-iPhone5s和Sony-Xperia智能手机拍摄的；
    - 数据类型：街景照片；
    - 数据量级：1125张图片，覆盖了约1.6公里 x 1.6公里的区域；
    - 发布机构及时间：东京工业大学于2015年发布；
    - [项目地址](http://www.ok.ctrl.titech.ac.jp/~torii/project/247/)
    - [相关论文](http://www.ok.ctrl.titech.ac.jp/~torii/project/247/download/Torii-CVPR-2015-final.pdf)
- **OXFORD ROBOTCAR DATASET**
    - 项目简介：这个数据集是为自动驾驶研究而创建的。数据集包含了超过1000公里的驾驶数据，这些数据是在牛津市的各种天气和交通条件下收集的；
    - 数据类型：图像数据，2D和3D扫描数据，以及位置数据；
    - 数据量级：图像数据：19,556,490个，总计22.86TB；2D扫描数据：25,618,605个，总计255.95GB；3D扫描数据：3,226,183个，总计31.76GB；位置数据：16,414,154个，5.658GB
    - 发布机构及时间：由牛津大学的工程科学系于2017年发布；
    - [项目地址](https://robotcar-dataset.robots.ox.ac.uk/)
    - [相关论文](https://robotcar-dataset.robots.ox.ac.uk/images/robotcar_ijrr.pdf)，[相关论文2](https://robotcar-dataset.robots.ox.ac.uk/images/RCD_RTK.pdf)
- **DeepLoc**
    - 项目简介：大规模城市户外定位数据集。这个数据集是在大学校园周围收集的。数据集在一个跨度110×130米的区域内收集，机器人以不同的驾驶模式多次穿越；
    - 数据类型：RGB和深度图像，语义分割注释（包括十个类别：背景、天空、道路、人行道、草地、植被、建筑、杆和围栏、动态和其他），以及6-DoF位姿；
    - 数据量级：训练集总共有2737张图像，测试集总共有1173张图像；
    - 发布机构及时间：由德国弗莱堡大学的计算机科学系于2018年发布；
    - [项目地址](http://deeploc.cs.uni-freiburg.de/)
    - [相关论文](http://ais.informatik.uni-freiburg.de/publications/papers/radwan18ral.pdf)

#### 2.2.4 单体建筑照片

- ****Oxford5k Dataset****
    - 项目简介：Oxford5k Dataset是一个包含5062张高分辨率（1024 × 768）图像的数据集，这些图像主要是一些地标的照片。对于每个地标，选择了5个不同的查询区域。这五个查询用于平均任何单个查询的特性。
    - 数据类型：地标照片；
    - 数据量级：包含11个地标的5062张图片；
    - 发布机构及时间：由牛津大学工程科学系和美国硅谷微软研究院于2007年发布；
    - [项目地址](https://www.robots.ox.ac.uk/~vgg/data/oxbuildings/)
    - [相关论文](https://www.robots.ox.ac.uk/~vgg/publications/2007/Philbin07/philbin07.pdf)
- ****Paris6K Dataset****
    - 项目简介：主要是巴黎的地标建筑；
    - 数据类型：图片数据，从Flickr获取的；
    - 数据量级：包含了6,300张高分辨率（1024 × 768）的图片；
    - 发布机构及时间：牛津大学工程科学系，捷克技术大学布拉格机器感知中心，美国硅谷微软研究院，法国巴黎高等师范学院计算机实验室和法国国家信息学自动化研究所于2008年发布；
    - [项目地址](https://www.robots.ox.ac.uk/~vgg/data/parisbuildings/)
    - [相关论文](https://www.robots.ox.ac.uk/~vgg/publications/2008/Philbin08/)
- ****CMP Facade Database****
    - 项目简介：数据集包含了多种类型的图像数据，主要是建筑立面的图像。这些图像来自不同的地点，包括捷克的布拉格、瑞士的苏黎世、巴塞罗那、希腊、布达佩斯和美国等地。
    - 数据类型：建筑立面图像；
    - 数据量级：CMP-Prague包含213张图像；CMP-World包含99张图像；ZuBuD包含177张图像；ECP-World包含177张图像；
    - 发布机构及时间：捷克技术大学的机器感知中心（Center for Machine Perception, Czech Technical University in Prague）于2013年发布；
    - [项目地址](https://cmp.felk.cvut.cz/~tylecr1/facade/)
    - [相关论文](https://cmp.felk.cvut.cz/~tylecr1/papers/Tylecek-GCPR2013.pdf)，[相关论文2](https://cmp.felk.cvut.cz/~tylecr1/facade/CMP_facade_DB_2013.pdf)
- **Matterport3D**
    - 项目简介：一个大规模的RGB-D数据集，提供了表面重建、相机姿态以及2D和3D语义分割的注释；
    - 数据类型：建筑室内照片
    - 数据量级：包含了194,400张RGB-D图像的10,800个全景视图，覆盖了90个建筑规模的场景；
    - 发布机构及时间：由普林斯顿大学，斯坦福大学和慕尼黑工业大学于2017年发布；
    - [项目地址](https://niessner.github.io/Matterport/)
    - [相关论文](https://arxiv.org/pdf/1709.06158.pdf)
- **S3DIS（Stanford large-scale 3D Indoor Spaces Dataset）**
    - 项目简介：是一个大规模的室内空间3D数据集。
    - 数据类型：主要是图像和3D网格，2D和3D语义；
    - 数据量级：数据集包含6个大型室内区域，这些区域来自3个主要用于教育和办公的建筑。数据集包含总共70,496张常规RGB图像和1,413张全景RGB图像，以及它们对应的深度、表面法线、语义注释、全球XYZ OpenEXR格式和相机元数据。此外，数据集还提供了作为纹理网格的整个建筑的3D重建，以及相应的3D语义网格。数据集还包含这些区域的彩色3D点云数据，总共有695,878,620个点。
    - 发布机构及时间：斯坦福大学和加州大学伯克利分校发布于2017年；
    - [项目地址](https://github.com/alexsax/2D-3D-Semantics)
    - [相关论文](https://arxiv.org/abs/1702.01105)
- **University1652-Baseline**
    - 项目简介：University-1652数据集包含了1652座建筑物的数据，其中1402座建筑物包含了所有三种视角（卫星视角、无人机视角和地面视角）的图像，而另外250座建筑物则缺少3D模型或街景图像；
    - 数据类型：卫星、无人机和手机相机拍摄的图片；
    - 数据量级：训练集：包含50,218张图片，覆盖701个类别（建筑物），涵盖33所大学。查询集（无人机视角）：包含37,855张图片，覆盖701个类别，涵盖39所大学。查询集（卫星视角）：包含701张图片，覆盖701个类别。查询集（地面视角）：包含2,579张图片，覆盖701个类别。图库集（无人机视角）：包含51,355张图片。图库集（地面视角）：包含2,921张图片，覆盖793个类别；
    - 发布机构及时间：由南方科技大学和悉尼科技大学发布于2020年；
    - [项目地址](https://github.com/layumi/University1652-Baseline)
    - [相关论文](https://arxiv.org/pdf/2002.12186v2.pdf)
- **WikiChurches**
    - 项目简介：主要覆盖了欧洲的教堂建筑，其中一半的教堂来自德国和法国；
    - 数据类型：图像数据；
    - 数据量级：包含了9485张图片，分为64个类别。每个类别的图片数量在1到3856之间；
    - 发布机构及时间：德国的耶拿大学于2021年发布；
    - [项目地址](https://zenodo.org/record/5166987)
    - [相关论文](https://arxiv.org/abs/2108.06959)
- **fire-load-detection**
    - 项目简介：一个由室内场景图像组成的数据集，所有图像中的实例都进行了注释并标记了材料类别；
    - 数据类型：室内图片；
    - 数据量级：包含1015张图像和8858个注释实例；
    - 发布机构及时间：由清华大学水土学院于2021年发布；
    - [项目地址](https://github.com/smartaec/fire-load-detection)
    - [相关论文](https://ieee-dataport.org/documents/idfire-image-dataset-indoor-fire-load-recognition)
- **SODA（Site Object Detection dAtaset）**
    - 项目简介：一个新的大规模图像数据集，专门为建筑工地收集和注释；
    - 数据类型：施工场地照片；
    - 数据量级：包含了19,846张图片，这些图片中包含了286,201个对象。这些对象被分为15个类别进行了标注。这些类别包括：工人（Worker）、材料（Material）、机器（Machine）、布局（Layout）、人（person）、安全帽（helmet）、背心（vest）、木板（board）、木材（wood）、钢筋（rebar）、砖块（brick）、脚手架（scaffold）、手推车（handcart）、切割机（cutter）、电箱（ebox）、料斗（hopper）、钩子（hook）、围栏（fence）和标语（slogan）等。
    - 发布机构及时间：清华水土学院和华南理工发布于2022年；
    - [项目地址](https://pan.baidu.com/s/1vuWIOdBnb-U5F_JOxcZoBw?pwd=9cnh)
    - [相关论文](https://www.sciencedirect.com/science/article/abs/pii/S0926580522003727?via%3Dihub)

### 2.3 模型数据集

- **三维重建数据集（古建筑）**
    - 项目简介：数据集主要内容包括两部分数据：1）第一部分数据包含激光扫描数据和对应的图像数据。包括清华大学的三处建筑物场景（清华大学老校门、清华学堂、清华生命科学楼），使用Riegl-LMS-Z420i型激光扫描仪获取建筑物的真值数据，同时拍摄图像数据。数据集中包括激光真值数据、图像数据、摄像机投影矩阵。2）第二部分数据为中国四大佛教名山（五台、峨眉、九华、普陀）和两大道教名山（武当、青城）的典型古建筑图像数据；
    - 数据类型：包括激光扫描数据、图像数据和摄像机投影矩阵；
    - 数据量级：网页上并没有明确提供数据集的具体量级信息。但是，从提供的下载链接和文件大小来看，数据集的规模应该是相当大的。例如，其中一部分数据包括中国四大佛教名山（五台、峨眉、九华、普陀）和两大道教名山（武当、青城）的典型古建筑图像数据，每个数据集的大小都在1.3GB到3.6GB之间；
    - 发布机构及时间：由中国科学院自动化研究所模式识别国家重点实验室于2011年发布；
    - [项目地址](http://vision.ia.ac.cn/zh/data/index.html)
    - [相关论文](http://vision.ia.ac.cn/zh/publications/index.html)
- **Rome16K dataset**
    - 项目简介：提出了一种快速、简单的位置识别和图像定位方法，该方法利用了从大型互联网照片集合中估计的特征对应关系和几何结构；
    - 数据类型：图像和3D点云模型。从大量的互联网图片中重建3D点云模型；
    - 数据量级：16K；
    - 发布机构及时间：由康奈尔大学早于2013年发布；
    - [项目地址](http://www.cs.cornell.edu/projects/p2f/)
    - [相关论文](https://www.cs.cornell.edu/projects/p2f/docs/localization_eccv2010.pdf)
- **Architectural Cultural Heritage dataset（ArCH）**
    - 项目简介：这个数据集首次为研究社区提供了描述遗产场景的带注释的点云。这些点云被标记为10个类别，旨在通过自动识别建筑元素来支持和加速重建HBIM模型的3D几何形状的过程；
    - 数据类型：点云数据集，其中包含了使用TLS和摄影测量调查收集的数据，提供了语义地面真实标注；
    - 数据量级：训练数据集：总共约1.021亿个点；测试数据集：总共约3399万个点；
    - 发布机构及时间：由Politecnico di Torino, Università Politecnica delle Marche, FBK Trento（意大利），以及INSA Strasbourg（法国）于2020年发布；
    - [项目地址](http://archdataset.polito.it/)
    - [相关论文](https://isprs-archives.copernicus.org/articles/XLIII-B2-2020/1419/2020/isprs-archives-XLIII-B2-2020-1419-2020.pdf)
- **IFCNet**
    - 项目简介：该数据集包含了实体IFC文件的几何和语义信息。它涵盖了广泛的IFC类别，旨在增强BIM（建筑信息模型）领域特定软件产品之间的互操作性和信息交换。此数据集旨在为BIM模型的语义丰富性的机器学习和深度学习的性能标准化做出贡献；
    - 数据类型：IFC对象的几何信息和语义信息；
    - 数据量级：包含5551个训练集，2379个测试集；
    - 发布机构及时间：由德国的RWTH Aachen University的Energy Efficiency and Sustainable Building E3D研究所于2020年发布；
    - [项目地址](https://ifcnet.e3d.rwth-aachen.de/)
    - [相关论文](https://arxiv.org/pdf/2106.09712v1.pdf)
- **BuildingNet**
    - 项目简介：BuildingNet是一个包含一致标签的3D建筑模型数据集，通过分析几何原始体的空间和结构关系来标记建筑网格；
    - 数据类型：3D建筑模型数据；
    - 数据量级：513K个标注的网格原始体，分组成292K个语义部分组件，跨越2K个建筑模型；
    - 发布机构及时间：于2021年发布；
    - [项目地址](https://buildingnet.org/)
    - [相关论文](https://arxiv.org/pdf/2110.04955v1.pdf)
- ****Habitat Matterport Dataset（HM3D）****
    - 项目简介：HM3D是迄今为止最大的3D室内空间数据集，包含了1000个高分辨率的3D扫描，涉及住宅、商业和公共空间。研究人员可以使用Habitat模拟器，大规模地训练具体化的代理，如家庭扫地机器人和AI助手；
    - 数据类型：建筑室内3D网格模型；
    - 数据量级：1000个近乎完整的高保真度的整个建筑的重建。包含了超过10600个房间，跨越大约1920个建筑楼层，可导航区域为112.5k平方米；
    - 发布机构及时间：由Facebook AI Research于2021年发布；
    - [项目地址](https://aihabitat.org/datasets/hm3d/)
    - [相关论文](https://arxiv.org/abs/2109.08238)
- **SUM: A Benchmark Dataset of Semantic Urban Meshes**
    - 项目简介：一个新的城市语义网格基准数据集，覆盖了芬兰赫尔辛基约4平方公里的区域，包含六个类别：地形、植被、建筑、水、车辆和船。
    - 数据类型：3D网格数据。此外，还提供了带有语义、颜色和对应面ID的采样点云；
    - 数据量级：总共标记了19,080,325个三角面；
    - 发布机构及时间：由荷兰代尔夫特理工大学发布于2021年；
    - [项目地址](https://3d.bk.tudelft.nl/projects/meshannotation/#data-split)
    - [相关论文](https://www.sciencedirect.com/science/article/pii/S0924271621001854)
      
### 2.4 结构化数据集

- **BDG2（building-data-genome-project-2）**
    - 项目简介：这是一个开源项目，旨在提供大量的建筑能源使用数据，以便研究人员可以使用这些数据进行各种分析和研究。数据集可能包括建筑的各种特性，如建筑类型、大小、地理位置等，以及详细的能源使用数据；
    - 数据类型：这个数据集包含了一些与建筑能源使用相关的数据，例如每日能源消耗（kWh）或水消耗（升）等。此外，这个数据集还包含了一些天气数据，例如外部空气温度（摄氏度）等；
    - 数据量级：n/a
    - [项目地址](https://github.com/buds-lab/building-data-genome-project-2)
    - [相关论文](https://arxiv.org/pdf/2006.02273.pdf)

## 3. 相关大模型

- **司空（Sikong）：基于中文建筑行业知识的LLaMA和Alpaca微调大模型**
    - 项目简介："Sikong" 是一个开源项目，它基于中文建筑行业知识对LLaMA和Alpaca模型进行了微调。这个项目通过收集建筑行业基础资料，构建了建筑行业数据集，并对LLaMA进行了指令微调，从而提高了LLaMA在中文建筑领域的问答效果。
    - [Web Demo](http://region-9.seetacloud.com:33955/)
    - [项目地址](https://github.com/SikongSphere/sikong)
