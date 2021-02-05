# 第四课：在游戏基础场景中展示一些内容

## 第一步： 设计显示游戏的 FPS 
接下来我们就要在游戏场景里展示点东西了，在显示点什么之前，我们先指定一下我们游戏的刷新率，你总是最关心游戏的刷新率不是吗？我们之前设计了一个刷新率变量 FPS ，它是30，这是我们给程序预定刷新率目标。为了实现这个目标，我们需要有个时钟来控制它。pygame给提供了一个时钟 Clock 子对象。我们在 `while` 前声明一个变量：
```
# 先取到pygame提供的Clock对象
clock = pygame.time.Clock()
```
有了这一行代码，我们就有了一个可操作的时钟对象。我们在`while`循环里面使用这个对象来控制刷新率。
让我们在的后面加入这行代码，注意代码前面的空格，一定要超过`while`的位置，否则就不算`while`的循环内代码了。在“while”里面（不要在“for”里面，不然每一次while里面就会执行很多次tick()方法）
```
    # keep loop running at the right speed
    clock.tick(FPS)
```
clock这个时钟对象有一个tick()方法，他只接受一个整数作为参数，所以我们把我们之前定义好的 FPS 这个变量传给他，它就会在pygame.time.Clock()方法里定义预定的刷新率。

<br>整体看一下我们的程序变成了什么样！
```
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
```
这里可以尝试一下重新运行程序，你会发现其实没有什么变化，但实际上我们在背后设定了每秒刷新窗口30次，而不是无限制的靠`while`循环的次数来决定每秒刷新多少次。

## 第二步： 定义一个程序内负责显示某个东西的“类”
如果我们想让窗口里显示一些东西，而且希望这个被显示的东西未来是可以控制的，那么我们最好按照面向对象的思路，先定一个“类”。在现实世界中，猫可以是一个“类”，猫长得每个都不一样但它们都是“猫”，性格不一样，如果一只猫很不幸死去了，我们永远没法再得到这只猫，而是再找一只其它“猫”，即使它们长得一摸一样。所以程序世界里也一样，我们先定义一个“类”把它命名为Player，每次我们让它进入小窗口表演，我们就基于这个类生成一个对象，这个对象负责在窗口上任意表现，等到我们不再需要它或是窗口关闭掉，我们就放弃这个对象，下次再有窗口的时候，你再基于“类”重新生成一个一摸一样的就好。那么我们在定义那些基础变量的程序后面加上这样一段定义：
```
class Player(pygame.sprite.Sprite):
    # 根据传统编程习惯，我们通常管那些用于显示时展示自我的“不知什么东西”叫做Sprite，英文精灵的意思。
    #定义一个初始化自己，self在程序里指我自己这个对象。
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        self.rect.clip
```
这里我们定义了一个叫做“Player”的类，我们将来会用它来在窗口表演，所以我们让它接收了一个pygame这个类提供的 sprite 这个对象。这个对象里有一个子对象，是真正最终表演者 Sprite。
<br>而且我们给 Player 这个类定义了两个方法，一个 `__init__` 一个 `update`。 为什么“__init__”这个方法命名的这么奇怪呢？这是根据程序员之间默认的习惯。将内部自己使用的方法加上“__”这样可以告诉别人我并不希望外部调用这个方法，我只是让对象自己给自己用而已。而update() 这个方法是我们希望外部来使用的。
<br>目前`__init__`方法只做了一件事，它用 pygame 这个类里面的Sprite子类的"__init__()"方法把自己（self）init（初始化）了一下，因为这个动作Player把自己变成了一种符合pygame要求的Sprite子对象。这样它就可以按照 pygame 给予的方法在 pygame 给搭建的“舞台”，这个小窗口表演了。而`update`方法更简单，因为它通过Sprite的init初始化过了，所以它就可以用Sprite的update()方法来更新自己。
<br>而`update()`这个方法则做对Player的具体对象做了一个显示更新。这里面self.rect代表自己所在的位置，而flip英文意思是“轻弹”，代表通过一个动作确认展示pygame的显示结果。在后面`pygame.display.flip()`我们会发现，整个pygame的display属性也有这样一个flip()方法。
<br>定义了完整的Player的行为方式，接下来当然就是告诉窗口，窗口中的Sprite，或者在这里被重新定义为Player这个类。这个类新生代对象“演员”登台以后应该怎么表演了。在`while`的上面加上几行 pygame 标准的操作。
```
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
```
这里我们定义了3个对象，all_sprites代表所有的表演者，我们用`pygame.sprite.Group()`这个方法来获取pygame 里提供的给表演者编组的方法。然后我们就可以用pygame提供的add()方法把表演者加进去。需要被加入进来的是player这个表演者，而 player 则使用我们在上面自己定义的“类” Player来定义。现在表演者已就位。我们要做的就是每次循环的时候都让它出现一下，那么在`while`循环里加入三句。`all_sprites.update()`，all_sprites会用pygame group自有的方法来调用所有参演对象的update()方法。
`all_sprites.draw(screen)`,all_sprites还有一个方法叫做`draw()`，“draw“方法是用来重画对象用的，这里面被输入的参数是`screen`，这就是需要程序刷新的窗口，而这个窗口是我们最开始定义给pygame的。如果你已经不记得了，你可以使用鼠标右键（在Mac上还可以用两个手指在触控版上点一下）点一下这个`screen`，然后在弹出菜单中选择`Go to Definition`来找到定义它的位置。
`pygame.display.flip()`，上面一句的draw代表在后台显示区里进行绘画计算，因为通常我们并不在窗口上完成draw这个过程，因为这会让显示慢的一塌糊涂。因此我们先在后台画好，然后flip一下让它真的显示出来。你还可以考虑用update()这个方法来代替flip，这两个方法一个是区域更新，一个是整个screen窗口更新，当一个图像固定展示时，这个变化不大，但是如果是一些目标持续变化时，他们就会有所不同。

<br>所以整个程序就变成了这样：
```
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        self.rect.flip

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
```
怎么样你写的和上面一样吗？执行一下，有错误吗？如果写的和上面一样你会发现，虽然窗口运行了，可是还是没有任何内容出来。player究竟在哪？其实它已经出来表演了，可是你既没有给它形状，也没有给它颜色，还没有给它任何动作，所以你看不见它。😄 别着急，下面就让我们给player这个表演者规定一下形象把。

## 第三步：给player穿上它的戏装
为了后面编程更加清晰，我们先增加几个定义！在你定义的长宽（WIDTH,HIGH）之类的变量的后面增加，下面几行：
```
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
```
就像以前跟你提前过的，对于计算机来说，颜色其实也只是代表了三原色的一些数字而已，这些数字都在0～255之间。虽然真正操作系统在定义输出时，比这个定义更加复杂，但是基本上我们开发时，python或是其它的语言都把他们翻译成代表红黄蓝的三个255以内的数字。0是最深，数字越高颜色越浅。所以(0, 0, 0)就是全黑，(255, 255, 255)就是全白。那么给了你上面这些定义，你就可以自己猜猜每个数字位置代表的是什么颜色喽。接下来我们会将 player 定义成绿色（0，255，0），你可以尝试自己挑一个颜色替换给 player。所以我们到Player类的`__init__()`方法里给它加一些定义，把init方法改成如下定义：
```
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
```
猜一猜我们都定义了什么！在之前的程序定义时，我们通过init将Player自己`self`初始化成了Sprite。这次。我们用Sprite提供的 image 方法给自己加了一个形状，这个形状是通过 pygame提供的Surface()方法提供的，Surface可以接收一个两个数的数组，其它他们代表了高和宽，现在Player类规定了，所有的表演者在初始化的时候要变成一个长50，宽50的方块。为什么有两层(())?因为Surface只接受一个参数，而这个参数是(50,50)这个数组，这样说能不能理解？你也可以理解为，Surface只接受一个方块，而50，50是这个方块的描述。
<br>然后接下来我们把self用image定义成方块之后，还要在定义它的颜色，所以我们用 `self.image.fill()` 这个方法给它填满颜色。
<br>有了形状和颜色，我们需要规定Player类的行为方式。要让他行为我们得先知道它的中心在哪里，不然我们就没办法非常准确的操作它的行为。所以我们用了 `self.image.get_rect()`这个方法，把刚刚定义好的image的中心，作为整个Player的中心。操作Player就等同于操作刚才定义的属于Player的那个图形。然后再把他的中心点放到整个窗口的中间。按照你学习长方形的数学知识，你可以很容易理解，长方形的中心，就在长的中间和宽的中间那个位置对吧？所以是 width/2,height/2。把这个值赋予`self.rect.center`意味着让刚才赋予self的那个image的中心位置将被设置到窗口的中间。
<br>现在如果执行程序，我们将看到一个停在窗口中心的绿色方块。它的大小是50个像素高，50个像素宽。一个像素就是咱们屏幕设置的分辨率的一个点。比如说，咱们把显示分辨率设置为1024*768，那么一个像素的大小就是屏幕宽的1/1024，高的1/768。


## 第四步：让演员“走位”
这节课的程序已经可以执行了，但是我们那可怜的“演员”，那个傻呆呆的绿色小方块，只能孤单单的站在舞台中央，什么也不会干。好吧，我们至少让它有些简单的走位。在Player的定义中，我们把updat做一个小小的调整。改成以下代码：
```
    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0
```
你可以看到我们可怜的小演员变成了一条长长的轨迹，有没有想起贪吃蛇？它究竟在做什么？它每一次update的时候，都把自己的中心位置“+”了5个像素。这就是`self.rect.x +=5`干的事情。实际上 “+=” 是程序员们一个特殊的写法，它相当于 `self.rect.x = self.rect.x + 5`。看一些简单的写法能让代码少很多，而且偷偷告诉你，它其实还能让CPU在计算的时候少生成一个 self.rect.x 的复制对象。当程序复杂到一定程度，这种节省是很有必要的。
<br>然后我们还加了一个`if`判断，你可以自己猜一下这个判断是什么意思！
<br>.
<br>.
<br>是的，这里的判断是告诉Player，如果你的长度超过了窗口的宽度“WIDTH”，那么让它的位置变成“0”，就是窗口的开始位置。
<br>可是这为什么让一个小方块变成了“贪吃蛇”呢？这是因为我们没有清除之前的小方块显示，又画了一个新的，慢慢的它就变成了一条线。怎么办？怎么让它变成移动而不是“贪吃蛇”？很遗憾，答案很粗暴！我们把整个窗口重新画一遍就好了。在`all_sprites.draw(screen)`绘制整个窗口之前，我们把整个窗口重新画成黑的。加入如下代码
```
    screen.fill(BLACK)
```
这时候还没有draw窗口，所以我们把它全涂成黑色就盖住了之前的绿色，然后在重新draw窗口加上player，现在我们的绿色小演员已经可以跑位了！

## 结束动作：别忘了把今天的工作放到Github上
### 要不要尝试一下使用其它颜色？
### 要不要尝试一下编写一个新的走位？
### 要不要尝试一下增加一个演员？这个很难，如果不成功，没关系。你可以考虑上完后面的课程再试。

参考第一课中的[结束动作](./FirstClass.md)将今天完成的程序也放到Github上。

## 回顾一下这一课都做了什么吧
### 理解一下判断、循环逻辑，特别是不同的循环执行方式的不同

### 理解一下属性与方法
到现在为止，这一节课是最复杂且内容最多的，如果能很好理解这一节课，后面的内容会变得很简单。如果不能完全理解，那也没关系。在后面的课程中，我们会更详细，更深入的使用这节课里的内容。

## [下一课，第五课](./class5.md)
## [回到主课程](./README.md)
