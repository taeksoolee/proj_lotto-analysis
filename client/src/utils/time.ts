
type Sleep = (ms: number) => Promise<void>;
export const sleep: Sleep = (ms) => {
  return new Promise((res, _) => {
    setTimeout(() => {
      res();
    }, ms);
  });
}