# 使用autograd.grad()计算导数与偏导

代码

```python
import torch
from torch import autograd
 
x = torch.rand(3, 4)
x.requires_grad_()

y = torch.sum(x)
print("-"*30,"\n x= \n",x)
print("-"*30,"\n y= x_1 + x_2 + x_3 +... =\n",y)

print("-"*30,"\n dy/dx= ")
print(autograd.grad(outputs=y, inputs=x)[0])
print("-"*30,"\n dy/dx= ")
print(autograd.grad(outputs=y, inputs=x,grad_outputs=torch.ones_like(y))[0])



y = x[:,0] +x[:,1]**2
print("-"*30,"\n x= \n",x)
print("-"*30,"\n y=x[:,0] + x[:,1]**2 =\n",y)
grad3 = autograd.grad(outputs=y, inputs=x, grad_outputs=torch.ones_like(y), create_graph=True)[0]
grad4 = autograd.grad(outputs=grad3, inputs=x, grad_outputs=torch.ones_like(grad3))[0]
print("-"*30,"\n dy/dx= ")
print(grad3)
print("-"*30,"\n d2y/dx2=")
print(grad4)
print("-"*30)
```

输出为


```python
------------------------------ 
 x=
 tensor([[0.6896, 0.3966, 0.2412, 0.5902],
        [0.0767, 0.2957, 0.2829, 0.3379],
        [0.1813, 0.3087, 0.8247, 0.9677]], requires_grad=True)
------------------------------
 y= x_1 + x_2 + x_3 +... =
 tensor(5.1931, grad_fn=<SumBackward0>)
------------------------------
 dy/dx=
tensor([[1., 1., 1., 1.], 
        [1., 1., 1., 1.], 
        [1., 1., 1., 1.]])
------------------------------ 
 dy/dx=
tensor([[1., 1., 1., 1.],      
        [1., 1., 1., 1.],
        [1., 1., 1., 1.]])
------------------------------
 x=
 tensor([[0.6896, 0.3966, 0.2412, 0.5902],
        [0.0767, 0.2957, 0.2829, 0.3379],
        [0.1813, 0.3087, 0.8247, 0.9677]], requires_grad=True)
------------------------------
 y=x[:,0] + x[:,1]**2 =
 tensor([0.8468, 0.1642, 0.2765], grad_fn=<AddBackward0>)
------------------------------
 dy/dx=
tensor([[1.0000, 0.7931, 0.0000, 0.0000],
        [1.0000, 0.5914, 0.0000, 0.0000],
        [1.0000, 0.6174, 0.0000, 0.0000]], grad_fn=<AddBackward0>)
------------------------------
 d2y/dx2=
tensor([[0., 2., 0., 0.],
        [0., 2., 0., 0.],
        [0., 2., 0., 0.]])
------------------------------
```