# 使用autograd.grad()计算导数与偏导


```python
import torch
from torch import autograd
 
x = torch.rand(3, 4)
x.requires_grad_()

y = torch.sum(x)
print(x)
print(y)
print(autograd.grad(outputs=y, inputs=x)[0])
print(autograd.grad(outputs=y, inputs=x,grad_outputs=torch.ones_like(y))[0])


y1 = x[:,0] +x[:,1]**2
print(x)
print(y1)
grad3 = autograd.grad(outputs=y1, inputs=x, grad_outputs=torch.ones_like(y1), create_graph=True)[0]
grad4 = autograd.grad(outputs=grad3, inputs=x, grad_outputs=torch.ones_like(grad3))[0]
print(grad3)
print(grad4)
```

输出为


```python
tensor([[0.3988, 0.9059, 0.3638, 0.7512],
        [0.3564, 0.8536, 0.4554, 0.8589],
        [0.2939, 0.1318, 0.8900, 0.3293]], requires_grad=True)
tensor(6.5891, grad_fn=<SumBackward0>)
tensor([[1., 1., 1., 1.], 
        [1., 1., 1., 1.], 
        [1., 1., 1., 1.]])
tensor([[1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.]])
tensor([[0.3988, 0.9059, 0.3638, 0.7512],
        [0.3564, 0.8536, 0.4554, 0.8589],
        [0.2939, 0.1318, 0.8900, 0.3293]], requires_grad=True)
tensor([1.2195, 1.0851, 0.3113], grad_fn=<AddBackward0>)
tensor([[1.0000, 1.8119, 0.0000, 0.0000],
        [1.0000, 1.7073, 0.0000, 0.0000],
        [1.0000, 0.2635, 0.0000, 0.0000]], grad_fn=<AddBackward0>)
tensor([[0., 2., 0., 0.],
        [0., 2., 0., 0.],
        [0., 2., 0., 0.]])
```