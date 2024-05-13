export default function guardrail (mathFunction) {
  const queue = [];
  let result;

  try {
    result = mathFunction();
  } catch (error) {
    result = `Error: ${error.message}`;
  } finally {
    queue.push(result);
    queue.push('Guardrail was processed');
  }

  return queue;
}
