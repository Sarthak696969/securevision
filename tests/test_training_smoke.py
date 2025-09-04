from securevision.queue.tasks.train import train_resnet18_tiny

def test_train_smoke():
    res = train_resnet18_tiny(epochs=1, batch_size=8)
    assert "val_acc" in res
